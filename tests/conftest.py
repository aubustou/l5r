from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from l5r_auto.cards.followers.common import Follower
from l5r_auto.cards.holdings.common import Holding
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.cards.strategies.common import Strategy
from l5r_auto.cards.strongholds.common import Stronghold
from l5r_auto.clans import CrabClan
from l5r_auto.deck import Deck
from l5r_auto.legality import TwentyFestivalsEdition
from l5r_auto.locations import Hand, PlayArea

# ---------------------------------------------------------------------------
# Module-level test card templates (registered in CARDS on import)
# IDs 90000–90099 reserved for shared fixtures
# IDs 91xxx / 92xxx used by _make_test_deck for minimal_game players
# ---------------------------------------------------------------------------

_STRONGHOLD = Stronghold(
    card_id=90000,
    title="Test Stronghold",
    gold_production="3",
    starting_family_honor=20,
    province_strength=7,
    clan=[CrabClan],
    legality=[TwentyFestivalsEdition],
)
_STRONGHOLD2 = Stronghold(
    card_id=90001,
    title="Test Stronghold 2",
    gold_production="2",
    starting_family_honor=20,
    province_strength=6,
    clan=[CrabClan],
    legality=[TwentyFestivalsEdition],
)
_PERSONALITY = Personality(
    card_id=90010,
    title="Test Samurai",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[CrabClan],
    legality=[TwentyFestivalsEdition],
)
_CHEAP_PERS = Personality(
    card_id=90011,
    title="Test Recruit",
    force=1,
    chi=1,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[CrabClan],
    legality=[TwentyFestivalsEdition],
)
_HOLDING = Holding(
    card_id=90020,
    title="Test Holding",
    gold_cost=2,
    gold_production="3",
    legality=[TwentyFestivalsEdition],
)
_HOLDING2 = Holding(
    card_id=90021,
    title="Test Holding 2",
    gold_cost=2,
    gold_production="2",
    legality=[TwentyFestivalsEdition],
)
_STRATEGY = Strategy(
    card_id=90030,
    title="Test Strategy",
    gold_cost=0,
    focus_value=2,
    legality=[TwentyFestivalsEdition],
)
_FOLLOWER = Follower(
    card_id=90040,
    title="Test Follower",
    force=1,
    chi=0,
    gold_cost=2,
    focus_value=1,
    legality=[TwentyFestivalsEdition],
)


def _make_test_deck(stronghold: Stronghold, prefix: int) -> Deck:
    """Build a minimal Deck with 6 personalities and 6 strategies using unique IDs."""
    personalities = [
        Personality(
            card_id=prefix + i,
            title=f"Deck Warrior {prefix + i}",
            force=2,
            chi=2,
            personal_honor=0,
            gold_cost=3,
            honor_requirement=None,
            clan=[CrabClan],
            legality=[TwentyFestivalsEdition],
        )
        for i in range(6)
    ]
    strategies = [
        Strategy(
            card_id=prefix + 10 + i,
            title=f"Deck Strategy {prefix + 10 + i}",
            gold_cost=0,
            focus_value=1,
            legality=[TwentyFestivalsEdition],
        )
        for i in range(6)
    ]
    deck = Deck(clan=CrabClan, legality=TwentyFestivalsEdition)
    deck.stronghold = stronghold
    deck.personalities = personalities
    deck.strategies = strategies
    return deck


# ---------------------------------------------------------------------------
# Session-level fixture: populate ALL_CARDS (needed for Deck.from_json)
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def _load_cards():
    from l5r_auto.cards import load_cards

    load_cards()


# ---------------------------------------------------------------------------
# Core mock fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_player():
    from l5r_auto.ai.heuristic_policy import HeuristicPolicy

    p = MagicMock()
    p.name = "TestPlayer"
    p.clan = CrabClan
    p.play_area = []
    p.hand = []
    p.fate_discard = []
    p.dynasty_discard = []
    p.fate_deck = []
    p.dynasty_deck = []
    p.removed_from_game = []
    p.entities = []
    # Real policy so decisions resolve to concrete picks (not MagicMock).
    p.policy = HeuristicPolicy()
    return p


@pytest.fixture
def mock_game(mock_player):
    g = MagicMock()
    g.entities = []
    g.current_player = mock_player
    return g


# ---------------------------------------------------------------------------
# Entity fixtures (function-scoped — fresh per test)
# ---------------------------------------------------------------------------


@pytest.fixture
def personality_entity(mock_game, mock_player):
    e = _PERSONALITY(game=mock_game, owner=mock_player)
    e.location = PlayArea
    e.face_down = False
    mock_player.play_area.append(e)
    mock_game.entities.append(e)
    return e


@pytest.fixture
def holding_entity(mock_game, mock_player):
    e = _HOLDING(game=mock_game, owner=mock_player)
    e.location = PlayArea
    e.face_down = False
    mock_player.play_area.append(e)
    mock_game.entities.append(e)
    mock_player.entities.append(e)
    return e


@pytest.fixture
def strategy_entity(mock_game, mock_player):
    e = _STRATEGY(game=mock_game, owner=mock_player)
    e.location = Hand
    e.face_down = False
    mock_player.hand.append(e)
    return e


@pytest.fixture
def follower_entity(mock_game, mock_player):
    e = _FOLLOWER(game=mock_game, owner=mock_player)
    e.location = Hand
    e.face_down = False
    mock_player.hand.append(e)
    return e


# ---------------------------------------------------------------------------
# Minimal real-game fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def minimal_game():
    """Real Game with 2 players — provinces filled and hands drawn, no StartOfGame run."""
    from l5r_auto.play import Game
    from l5r_auto.player import Player

    deck1 = _make_test_deck(_STRONGHOLD, prefix=91000)
    deck2 = _make_test_deck(_STRONGHOLD2, prefix=92000)

    p1 = Player(name="P1", deck=deck1)
    p2 = Player(name="P2", deck=deck2)

    # Game.__post_init__ calls player.create_entities(game) for both players
    game = Game(players=[p1, p2], legality=TwentyFestivalsEdition)

    for p in [p1, p2]:
        p.show_stronghold()
        p.set_starting_honor()
        p.shuffle_decks()
        p.create_provinces()  # pops 4 dynasty cards
        p.draw_hand()  # pops 5 fate cards

    game.starting_player = p1
    game.current_player = p1
    return game
