# CLAUDE.md — L5R Auto

## Project Overview

`l5r_auto` is a Python simulator and automated deck builder for the **Legend of the Five Rings (L5R) Collectible Card Game**. It models the full game engine: card definitions, deck construction, player state, turn phases, and game orchestration.

- **Package name**: `l5r_auto`
- **Python version**: 3.11
- **Author**: aubustou (survivalfr@yahoo.fr)

---

## Repository Layout

```
l5r/
├── pyproject.toml               # Build config, dependencies, entry points, tool settings
├── .pre-commit-config.yaml      # Pre-commit hooks (black, isort, autoflake, beautysh)
├── .gitignore                   # Excludes /decks and /reports output dirs
└── l5r_auto/
    ├── __init__.py
    ├── abilities.py             # Ability system, card actions, cost payment
    ├── build.py                 # Random deck builder (entry point: build_deck)
    ├── clans.py                 # Clan/faction class definitions
    ├── deck.py                  # Deck class: JSON serialization, card collection management
    ├── errors.py                # Custom exceptions
    ├── keywords.py              # Keyword definitions (100+ keywords as dataclasses)
    ├── legality.py              # Game format/edition legality definitions
    ├── locations.py             # Card location types (Hand, PlayArea, DynastyDiscard, etc.)
    ├── phases.py                # Game phases and turn lifecycle
    ├── play.py                  # Game orchestration (entry point: play)
    ├── player.py                # Player state and actions
    ├── rules.py                 # Rule enforcement utilities
    ├── utils.py                 # Dynamic submodule import helpers
    ├── models/
    │   └── __init__.py          # TypedDict definitions: GameReport, PlayerReport, EntityReport
    ├── cards/                   # Card definitions (~1000+ card files)
    │   ├── __init__.py          # Base classes: Card, Entity, DynastyCard, FateCard + registry
    │   ├── events/
    │   ├── followers/
    │   ├── holdings/
    │   ├── items/
    │   ├── personalities/
    │   ├── regions/
    │   ├── rings/
    │   ├── senseis/
    │   ├── spells/
    │   ├── strategies/
    │   └── strongholds/
    └── generate/
        ├── generate.py          # AST-based code generator from external Oracle API
        └── cards.json           # Cached card data from api.oracleofthevoid.com
```

**Runtime output directories** (excluded from git):
- `l5r_auto/decks/` — JSON deck files produced by `build_deck`
- `l5r_auto/reports/` — JSON game reports produced by `play`

---

## Entry Points

Defined in `pyproject.toml` under `[project.scripts]`:

| Command | Module | Purpose |
|---|---|---|
| `generate_code` | `l5r_auto.generate.generate:main` | Fetch card data from Oracle API, generate Python card files via AST |
| `build_deck` | `l5r_auto.build:main` | Build random legal decks for each clan, save to `decks/` |
| `play` | `l5r_auto.play:main` | Simulate games between random decks from `decks/`, save reports |

---

## Installation & Setup

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

---

## Development Workflow

### Code Style

All formatting is enforced by pre-commit hooks. Run before committing:

```bash
pre-commit run --all-files
```

Tools and their config (all in `pyproject.toml`):
- **black** — line length 88, target Python 3.11
- **isort** — `profile = 'black'`
- **autoflake** — removes all unused imports (respects `__init__.py` re-exports)
- **beautysh** — shell script formatting

### Running the Simulation

```bash
# 1. Generate card data (requires cards.json to already exist in generate/)
generate_code

# 2. Build decks
build_deck

# 3. Run a game simulation
play
```

### Logging

All simulation output uses Python's `logging` module. The `play` entry point sets `logging.basicConfig(level=logging.DEBUG)`. No separate test suite exists; behavior is validated via log output during simulation.

---

## Architecture

### Card System

Cards are the central abstraction. The hierarchy:

```
BaseCard          (title, keywords, traits, abilities)
└── Card          (card_id, legality, entity_type)
    ├── DynastyCard   (province placement)
    └── FateCard      (gold_cost, focus_value)
        → Personality, Holding, Event, Stronghold, Region,
          Strategy, Follower, Item, Sensei, Spell, Ring
```

- **Card registry** (`CARDS`, `ALL_CARDS` in `cards/__init__.py`): populated on first access via `load_cards()`, which dynamically imports all submodules.
- **Card → Entity instantiation**: calling a `Card` instance (e.g., `my_card(game=g, owner=p)`) creates a live `Entity` — the in-play representation of that card.
- Card files are organized by type → clan → edition, e.g. `cards/personalities/crab/twenty_festivals.py`.

### Entity System

`Entity` is the runtime instance of a `Card`:

```python
entity.bow()           # Set bowed=True
entity.straighten()    # Set bowed=False
entity.discard()       # Move to dynasty/fate discard pile
entity.move_to(loc)    # Explicitly set location
entity.can_produce     # True if in play, face-up, unbowed, has gold_production
```

Location changes update the owning player's collection lists (e.g., `player.play_area`, `player.hand`).

### Game Flow

```
Game.start()
├── StartOfGame
│   ├── ShowStrongholds      (A) Reveal strongholds/sensei, set starting honor
│   ├── DetermineStartingPlayer (B) Highest honor goes first (random on tie)
│   ├── ShuffleDecks         (C) Shuffle dynasty and fate decks
│   ├── CreateProvinces      (D) Create 4 provinces, fill from dynasty deck
│   ├── DrawCards            (E) Draw 5 fate cards
│   └── PlayGame             (F) Begin turn cycle
└── TurnSequences (loops up to MAX_NUMBER_OF_TURNS=50)
    └── Turn
        ├── StartPhase       Reveal provinces, trigger start-phase abilities
        ├── StraightenPhase  Straighten stronghold, sensei, and all play area cards
        ├── EventPhase       Activate face-up events in provinces
        ├── ActionPhase      Play affordable Strategy cards; attach Followers/Items to Personalities
        ├── AttackPhase      Attack a random opponent province with all unbowed Personalities;
        │                    resolve battle (force comparison); destroy province if attacker wins
        ├── DynastyPhase     Recruit affordable Personalities and Holdings from provinces
        ├── DiscardPhase     Discard random hand cards down to hand_size (5)
        ├── DrawPhase        Draw fate cards back up to hand_size
        └── EndPhase         Check honor ≥ 40 (HonorVictory) or honor < 0 (dishonor loss)
```

Game ends when any of:
- `HonorVictory` — a player reaches 40 honor, or drops below 0 (opponent wins)
- `ProvinceConquestVictory` — all 4 opponent provinces destroyed
- `EndOfDynastyDeckError` — dynasty deck exhausted
- `MaximumNumberOfTurnsReached` — 50 turn cap (`MAX_NUMBER_OF_TURNS` in `phases.py`)
- `EndOfFateDeckError` — gracefully handled mid-game; draw phase simply stops drawing

### Victory Conditions

Three ways a game ends by design:

- **Honor Victory** (`HONOR_VICTORY_THRESHOLD = 40` in `phases.py`): checked each `EndPhase`. If any player's honor reaches 40 or higher, they win immediately.
- **Dishonor Loss** (honor `< 0`): also checked each `EndPhase`. If a player's honor drops below zero, their opponent wins.
- **Province Conquest** (`player.remaining_provinces <= 0`): checked in `AttackPhase._destroy_province()` after each successful attack. Destroying all 4 opponent provinces wins the game.

### Deck System (`deck.py`)

A `Deck` contains:
- `stronghold`: one `Stronghold` card
- `sensei`: optional `Sensei` card
- Dynasty deck: `personalities`, `holdings`, `events`, `regions`
- Fate deck: `strategies`, `followers`, `items`, `spells`, `rings`
- `legality`: the `Legality` edition format
- `version`: semantic version string

Decks serialize to/from JSON via `Deck.to_json()` / `Deck.from_json()`, stored in `l5r_auto/decks/`.

### Legality / Editions (`legality.py`)

Supported formats (mapped in `generate.py` `LEGALITY_TO_AST`):

| Constant | Format name |
|---|---|
| `ImperialEdition` | Clan Wars (Imperial) |
| `JadeEdition` | Hidden Emperor (Jade) |
| `GoldEdition` | Four Winds (Gold) |
| `DiamondEdition` | Rain of Blood (Diamond) |
| `LotusEdition` | Age of Enlightenment (Lotus) |
| `SamuraiEdition` | Race for the Throne (Samurai) |
| `CelestialEdition` | Destroyer War (Celestial) |
| `EmperorEdition` | Age of Conquest (Emperor) |
| `IvoryEdition` | A Brother's Destiny (Ivory) |
| `TwentyFestivalsEdition` | A Brother's Destiny (Twenty Festivals) |
| `OnyxEdition` | Onyx Edition |
| `ModernEdition` | Modern |

### Clans & Factions (`clans.py`)

Nine great clans: `CrabClan`, `CraneClan`, `DragonClan`, `LionClan`, `MantisClan`, `PhoenixClan`, `ScorpionClan`, `SpiderClan`, `UnicornClan`

Factions: `BrotherhoodOfShinsei`, `ShadowlandsFaction`, `NinjaFaction`, `SpiritFaction`, `NagaFaction`, `RatlingFaction`

### Card Generation (`generate/generate.py`)

The generator fetches card data from `api.oracleofthevoid.com`, parses it, and uses Python's `ast` module to write card definition files:

1. Reads `generate/cards.json` (cached card data)
2. Filters cards to three target editions: `EmperorEdition`, `OnyxEdition`, `TwentyFestivalsEdition`
3. Groups cards by type and clan/edition
4. Generates Python files using `ast.Assign` nodes — card instances are module-level variable assignments, not classes

To regenerate cards after updating `cards.json`:
```bash
generate_code
```

Generated files follow the pattern:
```python
from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Bushi
from l5r_auto.legality import TwentyFestivalsEdition

"Card flavor text or rules text"
Hida_Benjiro = Personality(card_id=1234, title="Hida Benjiro", force=3, chi=2, ...)
```

---

## Key Conventions

### Python Style
- `from __future__ import annotations` at the top of every module (enables forward references)
- `@dataclass(repr=False, kw_only=True)` is the standard class decorator for all game objects
- `TYPE_CHECKING` guards used for import cycle avoidance — actual imports are deferred inside functions or at module bottom
- `field(metadata={"is_written": True})` marks fields that serialize to JSON/deck format

### Adding New Card Types
1. Create `cards/<type>/common.py` with the new `Card` and `Entity` subclasses
2. Add import at the bottom of `cards/__init__.py` (see existing pattern)
3. Add type mapping to `generate.py` `TYPES_TO_AST` and `LEGALITY_TO_AST`

### Adding New Keywords
Keywords are `@dataclass` subclasses of `Keyword` in `keywords.py`. The generator will print missing keyword stubs if `check_keywords()` finds undefined names.

### Abilities
Abilities live in `abilities.py`. Each has:
- `gather_legal_target_entities(game, player)` — what cards this ability can target
- `pay_cost(game, entity)` — returns `True` if cost was paid successfully
- `get_effect(game, entity)` — applies the effect

The global `ABILITIES` dict (populated by `__init_subclass__`) allows phase-level ability queries.

Action abilities used by `ActionPhase`:
- `PlayStrategyAbility` — plays a `Strategy` card from hand, paying its gold cost; bows gold-producing Holdings/Stronghold
- `AttachFollowerAbility` — attaches a `Follower` from hand to a `PersonalityEntity` in play area
- `AttachItemAbility` — attaches an `Item` from hand to a `PersonalityEntity` in play area

Gold payment uses the `_pay_gold(game, player, gold_cost)` helper (in `abilities.py`), which bows the minimum set of unbowed gold-producing entities to cover the cost.

> **Pitfall — phase ability initialization**: `Phase` is a `@dataclass` with `abilities: list[Ability] = field(default_factory=list)`. A class-level `abilities = [...]` assignment on a subclass will be silently overwritten by `__init__`. Always initialize phase abilities in `__post_init__`, not as a class attribute:
> ```python
> def __post_init__(self, *args, **kwargs):
>     self.abilities = [PlayStrategyAbility(), ...]
> ```

---

## Known Limitations / TODOs (from code comments)

- `play.main()` has a TODO for CLI argument parsing and player name handling
- Deck building only produces decks for clans with enough cards for the selected legality
- Only 2-player games are supported at runtime
- The card generator's Oracle API fetch code is commented out; only local JSON re-generation is active
- `DynastyDiscardAction` is excluded from the AI — cards stay in provinces until a player can afford to recruit them (discarding all face-up cards regardless of cost prevented personalities from ever being recruited)
- Onyx Edition has no dedicated strongholds in the card data; `build.py` falls back to Emperor Edition strongholds
- Restricted card list is not implemented — any card legal for the edition can appear up to 3 copies
- Iaijutsu duels, Ring mechanics, and the Open/Interrupt ability stack are out of scope
- `Experienced` keyword overlay (transferring attachments from lower-XP to higher-XP personality) is implemented in `RecruitAction` but not fully tested

### Implemented Keyword Mechanics

| Keyword | Where enforced | Behaviour |
|---|---|---|
| `Unique` | `RecruitAction.gather_legal_target_entities` | Blocks recruiting if a personality with the same title is already in the play area |
| `Experienced` | `RecruitAction.get_effect` | Recruiting an Experienced personality replaces the lower-XP version already in play, transferring all attachments |
| `Resilient` | `AttackPhase._destroy_with_resilient` | Entity bows instead of being destroyed the first time; tracked per-entity via `_resilient_used` flag |
| `Expendable` | `PersonalityEntity.destroy` | Entity draws a fate card for its owner when destroyed |

---

## No Test Suite

There are no automated tests. Correctness is currently validated by running the simulation (`play`) and observing log output. When adding significant logic, add `logging.debug` / `logging.info` statements to trace execution.
