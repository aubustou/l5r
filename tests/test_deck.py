"""Tests for Deck construction and JSON serialization."""
from __future__ import annotations

import json

import pytest

from l5r_auto.clans import CrabClan
from l5r_auto.deck import Deck
from l5r_auto.legality import TwentyFestivalsEdition

from tests.conftest import _HOLDING, _PERSONALITY, _STRATEGY, _STRONGHOLD


@pytest.fixture
def empty_deck():
    deck = Deck(clan=CrabClan, legality=TwentyFestivalsEdition)
    deck.stronghold = _STRONGHOLD
    return deck


class TestDeckAdd:
    def test_add_personality(self, empty_deck):
        empty_deck.add(_PERSONALITY)
        assert _PERSONALITY in empty_deck.personalities

    def test_add_holding(self, empty_deck):
        empty_deck.add(_HOLDING)
        assert _HOLDING in empty_deck.holdings

    def test_add_strategy(self, empty_deck):
        empty_deck.add(_STRATEGY)
        assert _STRATEGY in empty_deck.strategies

    def test_add_unknown_type_raises(self, empty_deck):
        with pytest.raises(ValueError, match="Unknown card type"):
            empty_deck.add(_STRONGHOLD)  # Stronghold is not addable via add()


class TestDeckSerialization:
    def test_to_json_contains_stronghold_id(self, empty_deck):
        data = json.loads(empty_deck.to_json())
        assert data["stronghold"] == _STRONGHOLD.card_id

    def test_to_json_contains_personality_ids(self, empty_deck):
        empty_deck.add(_PERSONALITY)
        data = json.loads(empty_deck.to_json())
        assert _PERSONALITY.card_id in data["personalities"]

    def test_to_json_contains_clan_name(self, empty_deck):
        data = json.loads(empty_deck.to_json())
        assert data["clan"] == CrabClan.name

    def test_roundtrip_preserves_stronghold(self, empty_deck):
        empty_deck.add(_PERSONALITY)
        empty_deck.add(_HOLDING)

        restored = Deck.from_json(empty_deck.to_json())

        assert restored.stronghold.title == _STRONGHOLD.title

    def test_roundtrip_preserves_personality_count(self, empty_deck):
        empty_deck.add(_PERSONALITY)
        empty_deck.add(_PERSONALITY)

        restored = Deck.from_json(empty_deck.to_json())

        assert len(restored.personalities) == 2
