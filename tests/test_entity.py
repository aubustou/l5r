"""Tests for Entity state management and location movement."""
from __future__ import annotations

import pytest

from l5r_auto.locations import DynastyDiscard, FateDiscard, Hand, PlayArea


class TestBowStraighten:
    def test_bow_sets_bowed(self, personality_entity):
        personality_entity.bow()
        assert personality_entity.bowed is True

    def test_straighten_clears_bowed(self, personality_entity):
        personality_entity.bowed = True
        personality_entity.straighten()
        assert personality_entity.bowed is False

    def test_bow_is_idempotent(self, personality_entity):
        personality_entity.bow()
        personality_entity.bow()
        assert personality_entity.bowed is True


class TestFaceUp:
    def test_face_up_default_false(self, mock_game, mock_player):
        from tests.conftest import _PERSONALITY

        e = _PERSONALITY(game=mock_game, owner=mock_player)
        assert e.face_up is False

    def test_turn_face_up(self, mock_game, mock_player):
        from tests.conftest import _PERSONALITY

        e = _PERSONALITY(game=mock_game, owner=mock_player)
        e.turn_face_up()
        assert e.face_up is True

    def test_turn_face_down(self, personality_entity):
        # personality_entity fixture has face_down=False
        personality_entity.turn_face_down()
        assert personality_entity.face_up is False


class TestCanProduce:
    def test_can_produce_true(self, holding_entity):
        # holding_entity fixture: PlayArea, face_up, unbowed, gold_production set
        assert holding_entity.can_produce is True

    def test_can_produce_false_when_bowed(self, holding_entity):
        holding_entity.bowed = True
        assert holding_entity.can_produce is False

    def test_can_produce_false_when_face_down(self, holding_entity):
        holding_entity.face_down = True
        assert holding_entity.can_produce is False

    def test_can_produce_false_wrong_location(self, holding_entity):
        holding_entity.location = Hand
        assert holding_entity.can_produce is False

    def test_can_produce_false_no_gold_production(self, personality_entity):
        # Personalities have no gold_production attribute
        assert personality_entity.can_produce is False

    def test_can_produce_true_in_stronghold_location(self, mock_game, mock_player):
        from l5r_auto.locations import StrongholdLocation
        from tests.conftest import _STRONGHOLD

        sh = _STRONGHOLD(game=mock_game, owner=mock_player)
        sh.location = StrongholdLocation
        sh.face_down = False
        assert sh.can_produce is True


class TestMoveTo:
    def test_move_to_removes_from_old_list(self, personality_entity, mock_player):
        # starts in PlayArea / mock_player.play_area
        personality_entity.move_to(Hand)
        assert personality_entity not in mock_player.play_area

    def test_move_to_adds_to_new_list(self, personality_entity, mock_player):
        personality_entity.move_to(Hand)
        assert personality_entity in mock_player.hand

    def test_move_to_updates_location(self, personality_entity):
        personality_entity.move_to(Hand)
        assert personality_entity.location is Hand


class TestDiscard:
    def test_discard_fate_card_to_fate_discard(self, strategy_entity, mock_player):
        # StrategyEntity is a FateCard subclass
        strategy_entity.discard()
        assert strategy_entity in mock_player.fate_discard

    def test_discard_dynasty_card_to_dynasty_discard(
        self, personality_entity, mock_player
    ):
        # PersonalityEntity is a DynastyCard subclass
        personality_entity.discard()
        assert personality_entity in mock_player.dynasty_discard

    def test_discard_resets_bowed(self, strategy_entity):
        strategy_entity.bowed = True
        strategy_entity.discard()
        assert strategy_entity.bowed is False
