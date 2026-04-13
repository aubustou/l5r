"""Tests for Player initialization and deck-drawing mechanics."""
from __future__ import annotations

import pytest

from l5r_auto.clans import CrabClan
from l5r_auto.errors import EndOfDynastyDeckError, EndOfFateDeckError

from tests.conftest import _STRONGHOLD, _make_test_deck


@pytest.fixture
def minimal_deck():
    return _make_test_deck(_STRONGHOLD, prefix=93000)


class TestPlayerInit:
    def test_clan_set_from_deck(self, minimal_deck):
        from l5r_auto.player import Player

        player = Player(name="TestP", deck=minimal_deck)
        assert player.clan is CrabClan

    def test_stronghold_set_from_deck(self, minimal_deck):
        from l5r_auto.player import Player

        player = Player(name="TestP", deck=minimal_deck)
        assert player.stronghold is _STRONGHOLD

    def test_name_auto_generated_when_empty(self, minimal_deck):
        from l5r_auto.player import Player

        player = Player(name="", deck=minimal_deck)
        assert player.name != ""


class TestPlayerDrawCards:
    def test_draw_fate_card_raises_when_empty(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.fate_deck.clear()

        with pytest.raises(EndOfFateDeckError):
            p1.draw_fate_card()

    def test_draw_dynasty_card_raises_when_empty(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.dynasty_deck.clear()

        with pytest.raises(EndOfDynastyDeckError):
            p1.draw_dynasty_card()

    def test_draw_fate_card_moves_to_hand(self, minimal_game):
        from l5r_auto.locations import Hand

        p1 = minimal_game.players[0]
        # Add a card back to fate deck for drawing
        card = p1.hand.pop()
        card.location = type(card).location  # reset to Deck default
        p1.fate_deck.append(card)
        initial_hand_size = len(p1.hand)

        p1.draw_fate_card()

        assert len(p1.hand) == initial_hand_size + 1


class TestPlayerProvinces:
    def test_create_provinces_creates_four(self, minimal_game):
        p1 = minimal_game.players[0]
        # minimal_game already called create_provinces()
        assert len(p1.provinces) == 4

    def test_provinces_filled_with_dynasty_cards(self, minimal_game):
        p1 = minimal_game.players[0]
        for province in p1.provinces:
            assert len(province.dynasty_cards) == 1
