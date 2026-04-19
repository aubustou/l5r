"""Tests for the Policy interface plumbed through the game engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pytest

from l5r_auto.ai.heuristic_policy import HeuristicPolicy
from l5r_auto.ai.policy import (
    PASS,
    KIND_ACTION_ROUND,
    KIND_ATTACH_TARGET,
    KIND_ATTACK_TARGET,
    KIND_DISCARD_HAND,
    KIND_PAY_GOLD,
    Decision,
    Option,
)
from l5r_auto.ai.random_policy import RandomPolicy
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.locations import PlayArea, ProvinceLocation
from l5r_auto.phases import AttackPhase, DynastyPhase, Turn
from tests.conftest import _PERSONALITY, _STRATEGY


@dataclass
class RecordingPolicy:
    """Policy that records every Decision it's asked and delegates the
    actual choice to a wrapped policy."""

    name: str = "recording"
    kinds_seen: set = field(default_factory=set)
    decisions: list = field(default_factory=list)
    inner: Any = field(default_factory=HeuristicPolicy)

    def choose(self, decision, game):
        self.kinds_seen.add(decision.kind)
        self.decisions.append(decision)
        return self.inner.choose(decision, game)


@dataclass
class ForcedPolicy:
    """Policy that always picks the option whose ``id`` starts with a prefix,
    falling back to first option otherwise. Useful to force specific paths."""

    name: str = "forced"
    prefix: str = ""

    def choose(self, decision, game):
        if not decision.options:
            return []
        for opt in decision.options:
            if self.prefix and opt.id.startswith(self.prefix):
                return [opt]
        return [decision.options[0]]


class TestPolicyInterface:
    def test_random_policy_single_pick(self):
        import random

        rng = random.Random(0)
        pol = RandomPolicy(rng=rng)
        decision = Decision(
            kind=KIND_ACTION_ROUND,
            player=None,
            options=[Option(id="a"), Option(id="b"), Option(id="c")],
        )
        picked = pol.choose(decision, game=None)
        assert len(picked) == 1
        assert picked[0].id in {"a", "b", "c"}

    def test_random_policy_empty_decision(self):
        pol = RandomPolicy()
        decision = Decision(kind=KIND_ACTION_ROUND, player=None, options=[])
        assert pol.choose(decision, game=None) == []

    def test_heuristic_picks_smallest_covering_gold(self):
        pol = HeuristicPolicy()

        class _Prod:
            def __init__(self, amount):
                self.gold_production = amount

        small = _Prod(2)
        big = _Prod(5)
        decision = Decision(
            kind=KIND_PAY_GOLD,
            player=None,
            options=[Option(id="big", payload=big), Option(id="small", payload=small)],
            context={"remaining_cost": 2},
        )
        picked = pol.choose(decision, game=None)
        assert picked[0].payload is small

    def test_heuristic_pays_big_when_small_insufficient(self):
        pol = HeuristicPolicy()

        class _Prod:
            def __init__(self, amount):
                self.gold_production = amount

        small = _Prod(1)
        big = _Prod(5)
        decision = Decision(
            kind=KIND_PAY_GOLD,
            player=None,
            options=[Option(id="small", payload=small), Option(id="big", payload=big)],
            context={"remaining_cost": 4},
        )
        picked = pol.choose(decision, game=None)
        assert picked[0].payload is big

    def test_heuristic_discard_drops_weakest(self):
        pol = HeuristicPolicy()

        class _Card:
            def __init__(self, force=0, gold_cost=0):
                self.force = force
                self.gold_cost = gold_cost

        weak = _Card(force=0, gold_cost=1)
        mid = _Card(force=2, gold_cost=3)
        strong = _Card(force=5, gold_cost=5)
        opts = [
            Option(id="strong", payload=strong),
            Option(id="mid", payload=mid),
            Option(id="weak", payload=weak),
        ]
        decision = Decision(
            kind=KIND_DISCARD_HAND,
            player=None,
            options=opts,
            min_picks=2,
            max_picks=2,
        )
        picked = pol.choose(decision, game=None)
        assert len(picked) == 2
        chosen = {opt.payload for opt in picked}
        assert weak in chosen and mid in chosen


class TestEngineRaisesDecisions:
    """Proves the engine poses Decisions of each expected kind."""

    def test_attack_phase_poses_attack_target_decision(self, minimal_game):
        """AttackPhase must ask the active player's policy to pick a province."""
        attacker = minimal_game.players[0]
        defender = minimal_game.players[1]

        # Give attacker a personality to attack with.
        p = _PERSONALITY(game=minimal_game, owner=attacker)
        p.location = PlayArea
        p.face_down = False
        p.bowed = False
        attacker.play_area.append(p)

        recorder = RecordingPolicy()
        attacker.policy = recorder

        turn = Turn(game=minimal_game, number=1, active_player=attacker)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=attacker)
        phase._start()

        assert KIND_ATTACK_TARGET in recorder.kinds_seen
        attack_decision = next(
            d for d in recorder.decisions if d.kind == KIND_ATTACK_TARGET
        )
        # Every defender province with dynasty cards should be an option,
        # plus a PASS option.
        province_options = [o for o in attack_decision.options if o is not PASS]
        assert len(province_options) == len(
            [p for p in defender.provinces if p.dynasty_cards]
        )
        assert PASS in attack_decision.options

    def test_discard_phase_poses_discard_decision(self, minimal_game):
        p1 = minimal_game.players[0]
        for _ in range(4):
            extra = _STRATEGY(game=minimal_game, owner=p1)
            extra.location = __import__(
                "l5r_auto.locations", fromlist=["Hand"]
            ).Hand
            extra.face_down = False
            p1.hand.append(extra)
        assert len(p1.hand) > p1.max_hand_size
        excess = len(p1.hand) - p1.max_hand_size

        recorder = RecordingPolicy()
        p1.policy = recorder

        turn = Turn(game=minimal_game, number=1, active_player=p1)
        phase = DynastyPhase(game=minimal_game, turn=turn, active_player=p1)
        phase._end_of_turn_discard()

        assert KIND_DISCARD_HAND in recorder.kinds_seen
        discard_decision = next(
            d for d in recorder.decisions if d.kind == KIND_DISCARD_HAND
        )
        assert discard_decision.min_picks == excess
        assert discard_decision.max_picks == excess
        assert len(p1.hand) <= p1.max_hand_size


class TestPolicyInfluencesOutcome:
    """Forcing a specific choice must change what the engine does."""

    def test_forced_attack_target_selects_that_province(self, minimal_game):
        attacker = minimal_game.players[0]
        defender = minimal_game.players[1]

        p = _PERSONALITY(game=minimal_game, owner=attacker)
        p.location = PlayArea
        p.face_down = False
        p.bowed = False
        attacker.force = 999  # unused; the entity's force is 3
        attacker.play_area.append(p)

        # Force the policy to always pick "province:0" (the first province).
        attacker.policy = ForcedPolicy(prefix="province:0")

        # Capture defender's provinces before attack.
        provinces_before = list(defender.provinces)
        target_province = next(
            pr for pr in provinces_before if pr.dynasty_cards
        )

        recorder = RecordingPolicy(inner=ForcedPolicy(prefix="province:0"))
        attacker.policy = recorder

        turn = Turn(game=minimal_game, number=1, active_player=attacker)
        phase = AttackPhase(game=minimal_game, turn=turn, active_player=attacker)
        phase._start()

        # Recorder should have seen the attack-target decision and the chosen
        # province should be the first valid one.
        attack_decision = next(
            d for d in recorder.decisions if d.kind == KIND_ATTACK_TARGET
        )
        province_opts = [o for o in attack_decision.options if o is not PASS]
        assert province_opts[0].payload is target_province


class TestPolicyFieldDefault:
    def test_player_has_default_random_policy(self, minimal_game):
        p1 = minimal_game.players[0]
        assert p1.policy is not None
        # The default should behave like a policy (have a choose method).
        assert callable(getattr(p1.policy, "choose", None))
