"""Tests for game phase execution."""

from __future__ import annotations

import pytest

from l5r_auto.errors import HonorVictory, ProvinceConquestVictory
from l5r_auto.locations import Hand, PlayArea
from l5r_auto.phases import (
    ActionPhase,
    AttackPhase,
    DynastyPhase,
    Turn,
)
from tests.conftest import _PERSONALITY, _STRATEGY


def _make_turn(game, player):
    return Turn(game=game, number=1, active_player=player)


class TestStraightenPhase:
    """Straightening is now the first step of ActionPhase."""

    def test_straightens_play_area_cards(self, minimal_game):
        p1 = minimal_game.players[0]
        entity = _PERSONALITY(game=minimal_game, owner=p1)
        entity.location = PlayArea
        entity.face_down = False
        entity.bowed = True
        p1.play_area.append(entity)

        turn = _make_turn(minimal_game, p1)
        phase = ActionPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._straighten()

        assert entity.bowed is False

    def test_straightens_stronghold(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.stronghold_entity.bowed = True

        turn = _make_turn(minimal_game, p1)
        phase = ActionPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._straighten()

        assert p1.stronghold_entity.bowed is False


class TestVictoryChecks:
    """Honor Victory and Dishonor Loss are now checked on the Turn."""

    def test_no_exception_under_honor_threshold(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.honor = 19  # below threshold of 40

        turn = _make_turn(minimal_game, p1)
        # Should not raise
        turn._check_honor_victory()

    def test_honor_victory_at_40(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.honor = 40

        turn = _make_turn(minimal_game, p1)
        with pytest.raises(HonorVictory) as exc_info:
            turn._check_honor_victory()

        assert exc_info.value.winner is p1

    def test_dishonor_at_minus_20(self, minimal_game):
        p1 = minimal_game.players[0]
        p2 = minimal_game.players[1]
        p1.honor = -20

        turn = _make_turn(minimal_game, p1)
        with pytest.raises(HonorVictory) as exc_info:
            turn._check_dishonor_loss()

        assert exc_info.value.winner is p2

    def test_no_dishonor_at_minus_19(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.honor = -19

        turn = _make_turn(minimal_game, p1)
        # Should not raise
        turn._check_dishonor_loss()


class TestEndOfTurnDiscard:
    """Discard is now part of DynastyPhase._end_of_turn_discard."""

    def test_discards_excess_cards(self, minimal_game):
        p1 = minimal_game.players[0]

        for _ in range(4):
            extra = _STRATEGY(game=minimal_game, owner=p1)
            extra.location = Hand
            extra.face_down = False
            p1.hand.append(extra)

        assert len(p1.hand) > p1.max_hand_size

        turn = _make_turn(minimal_game, p1)
        phase = DynastyPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._end_of_turn_discard()

        assert len(p1.hand) <= p1.max_hand_size

    def test_no_discard_at_max_hand_size(self, minimal_game):
        p1 = minimal_game.players[0]
        original_count = len(p1.hand)
        assert original_count <= p1.max_hand_size

        turn = _make_turn(minimal_game, p1)
        phase = DynastyPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._end_of_turn_discard()

        assert len(p1.hand) == original_count


class TestEndOfTurnDraw:
    """Drawing is now part of DynastyPhase._end_of_turn_draw (draws exactly 1)."""

    def test_draws_one_card(self, minimal_game):
        from l5r_auto.locations import Deck

        p1 = minimal_game.players[0]

        # Ensure there's a card in the fate deck to draw
        if not p1.fate_deck:
            card = p1.hand.pop()
            card.location = Deck
            p1.fate_deck.append(card)

        initial_hand = len(p1.hand)
        initial_deck = len(p1.fate_deck)
        assert initial_deck >= 1

        turn = _make_turn(minimal_game, p1)
        phase = DynastyPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._end_of_turn_draw()

        assert len(p1.hand) == initial_hand + 1
        assert len(p1.fate_deck) == initial_deck - 1

    def test_stops_on_empty_fate_deck(self, minimal_game):
        p1 = minimal_game.players[0]
        p1.hand.clear()
        p1.fate_deck.clear()

        turn = _make_turn(minimal_game, p1)
        phase = DynastyPhase(game=minimal_game, turn=turn, active_player=p1)
        # Should not raise
        phase._end_of_turn_draw()

        assert len(p1.hand) == 0


class TestAttackPhaseHelpers:
    def _make_province(self, game, player):
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
        destroyed = phase._try_destroy(resilient_card)

        # First time: should bow, not destroy
        assert destroyed is False
        assert resilient_card.bowed is True
        assert resilient_card.location is PlayArea

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
        destroyed = phase._try_destroy(resilient_card)

        # Second time: should be destroyed
        assert destroyed is True
        assert resilient_card.location is not PlayArea
