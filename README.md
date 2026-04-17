# L5R Auto

An automated game simulator and deck builder for the **Legend of the Five Rings (L5R) Collectible Card Game**.

## What It Does

- **Generates** Python card definitions from the Oracle of the Void card database
- **Builds** random legal decks for each clan
- **Simulates** full games between two decks, logging the game state at every step

## Requirements

- Python 3.11+

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

### 1. Generate card data

Regenerates Python card files from the cached `generate/cards.json`:

```bash
generate_code
```

### 2. Build decks

Creates random legal decks for each clan and saves them as JSON under `l5r_auto/decks/`:

```bash
build_deck
```

### 3. Run a simulation

Picks two random decks from `l5r_auto/decks/` and simulates a game:

```bash
play
```

Game progress is printed to stdout via Python's `logging` module (DEBUG level).

## Project Structure

```
l5r_auto/
├── cards/          Card definitions organized by type → clan → edition
├── generate/       Code generator and cached card JSON from Oracle of the Void
├── models/         TypedDict schemas for game reports
├── abilities.py    Ability system and card actions
├── build.py        Deck builder
├── clans.py        Clan and faction definitions
├── deck.py         Deck class with JSON serialization
├── keywords.py     Keyword definitions (100+ keywords)
├── legality.py     Format/edition legality rules
├── locations.py    Card location types (hand, play area, discard, etc.)
├── phases.py       Turn phases and game lifecycle
├── play.py         Game orchestration
└── player.py       Player state and actions
```

## Supported Formats

Imperial, Jade, Gold, Diamond, Lotus, Samurai, Celestial, Emperor, Ivory, Twenty Festivals, Onyx, Modern

## Supported Clans

Crab, Crane, Dragon, Lion, Mantis, Phoenix, Scorpion, Spider, Unicorn  
Factions: Brotherhood of Shinsei, Shadowlands, Ninja, Spirit, Naga, Ratling

## Testing

```bash
pytest
# With coverage:
pytest --cov=l5r_auto --cov-report=term-missing
```

The `tests/` directory contains unit tests for abilities, phases, entities, players, and decks.

## CI

GitHub Actions runs three jobs on every push and pull request:
- **lint** — `ruff check` and `ruff format --check`
- **test** — `pytest --cov=l5r_auto --cov-report=term-missing`
- **build** — `python -m build`

## Development

```bash
# Install pre-commit hooks
pre-commit install

# Run all linters/formatters
pre-commit run --all-files
```

Code style: **black** (line length 88) + **isort** + **autoflake** (pre-commit)  
CI linting: **ruff** (`ruff check` + `ruff format --check`)

## License

See repository for license information.
