"""Tests for game phase execution."""
from __future__ import annotations

import pytest

from l5r_auto.errors import HonorVictory, ProvinceConquestVictory
from l5r_auto.locations import Deck as DeckLocation
from l5r_auto.locations import Hand, PlayArea, ProvinceLocation
from l5r_auto.phases import (
    AttackPhase,
    DiscardPhase,
    DrawPhase,
    EndPhase,
    StraightenPhase,
    Turn,
)

from tests.conftest import _PERSONALITY, _STRATEGY


def _make_turn(game, player):
    return Turn(game=game, number=1, active_player=player)


class TestStraightenPhase:
    def test_straightens_play_area_cards(self, minimal_game):
        p1 = minimal_game.players[0]
        # Recruit a personality into play area by manually placing one
        entity = _PERSONALITY(game=minimal_game, owner=p1)
        entity.location = PlayArea
        entity.face_down = False
        entity.bowed = True
        p1.play_area.append(entity)

        turn = _make_turn(minimal_game, p1)
        StraightenPhase(game=minimal_game, turn=turn, active_player=p1).start()

        assert entity.bowed is False

    def test_straightens_stronghold(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.stronghold_entity.bowed = True

        turn = _make_turn(minimal_game, p1)
        StraightenPhase(game=minimal_game, turn=turn, active_player=p1).start()

        assert p1.stronghold_entity.bowed is False


class TestEndPhase:
    def test_no_exception_under_honor_threshold(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.honor = 19  # below threshold of 40

        turn = _make_turn(minimal_game, p1)
        # Should not raise
        EndPhase(game=minimal_game, turn=turn, active_player=p1)._start()

    def test_honor_victory_at_40(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.honor = 40

        turn = _make_turn(minimal_game, p1)
        with pytest.raises(HonorVictory) as exc_info:
            EndPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert exc_info.value.winner is p1

    def test_dishonor_below_zero(self, minimal_game):
        p1 = minimal_game.players[0]
        p2 = minimal_game.players[1]
        p1.honor = -1

        turn = _make_turn(minimal_game, p1)
        with pytest.raises(HonorVictory) as exc_info:
            EndPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert exc_info.value.winner is p2


class TestDiscardPhase:
    def test_discards_excess_cards(self, minimal_game):
        p1 = minimal_game.players[0]

        # Add 2 extra strategy entities to hand (beyond hand_size)
        for i in range(2):
            extra = _STRATEGY(game=minimal_game, owner=p1)
            extra.location = Hand
            extra.face_down = False
            p1.hand.append(extra)

        assert len(p1.hand) == p1.hand_size + 2

        turn = _make_turn(minimal_game, p1)
        DiscardPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert len(p1.hand) == p1.hand_size

    def test_no_discard_at_hand_size(self, minimal_game):
        p1 = minimal_game.players[0]
        assert len(p1.hand) == p1.hand_size  # exactly at hand size

        turn = _make_turn(minimal_game, p1)
        DiscardPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert len(p1.hand) == p1.hand_size


class TestDrawPhase:
    def test_draws_up_to_hand_size(self, minimal_game):
        p1 = minimal_game.players[0]

        # Remove cards to leave exactly 2 in hand
        for _ in range(p1.hand_size - 2):
            card = p1.hand.pop()
            card.location = type(card).location  # reset to Deck default
            p1.fate_deck.append(card)

        assert len(p1.hand) == 2

        turn = _make_turn(minimal_game, p1)
        DrawPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert len(p1.hand) == p1.hand_size

    def test_stops_on_empty_fate_deck(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.hand_size = 5

        # Empty the hand and fate deck
        p1.hand.clear()
        p1.fate_deck.clear()

        turn = _make_turn(minimal_game, p1)
        # Should not raise, just draw nothing
        DrawPhase(game=minimal_game, turn=turn, active_player=p1)._start()

        assert len(p1.hand) == 0


class TestAttackPhaseHelpers:
    def _make_province(self, game, player):
        """Create a minimal province-like object for testing _destroy_province."""
        from unittest.mock import MagicMock

        province = MagicMock()
        province.dynasty_cards = []
        return province

    def test_destroy_province_decrements_remaining(self, minimal_game):
        attacker = minimal_game.players[0]
        defender = minimal_game.players[1]
        defender.remaining_provinces = 2

        province = self._make_province(minimal_game, defender)

        turn = _make_turn(minimal_game, attacker)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=attacker)
        phase._destroy_province(province, attacker, defender)

        assert defender.remaining_provinces == 1

    def test_destroy_last_province_raises_victory(self, minimal_game):
        attacker = minimal_game.players[0]
        defender = minimal_game.players[1]
        defender.remaining_provinces = 1

        province = self._make_province(minimal_game, defender)

        turn = _make_turn(minimal_game, attacker)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=attacker)

        with pytest.raises(ProvinceConquestVictory) as exc_info:
            phase._destroy_province(province, attacker, defender)

        assert exc_info.value.winner is attacker
        assert exc_info.value.loser is defender

    def test_resilient_bows_instead_of_destroy(self, minimal_game):
        from l5r_auto.keywords import Resilient

        p1 = minimal_game.players[0]

        resilient_card = _PERSONALITY(game=minimal_game, owner=p1)
        resilient_card.keywords = [Resilient]
        resilient_card.location = PlayArea
        resilient_card.face_down = False
        p1.play_area.append(resilient_card)

        turn = _make_turn(minimal_game, p1)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._destroy_with_resilient(resilient_card)

        # First time: should bow, not destroy
        assert resilient_card.bowed is True
        assert resilient_card.location is PlayArea  # still in play

    def test_resilient_destroys_second_time(self, minimal_game):
        from l5r_auto.keywords import Resilient

        p1 = minimal_game.players[0]

        resilient_card = _PERSONALITY(game=minimal_game, owner=p1)
        resilient_card.keywords = [Resilient]
        resilient_card.location = PlayArea
        resilient_card.face_down = False
        resilient_card._resilient_used = True  # already used
        p1.play_area.append(resilient_card)

        turn = _make_turn(minimal_game, p1)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._destroy_with_resilient(resilient_card)

        # Second time: should be destroyed (moved to discard)
        assert resilient_card.location is not PlayArea
