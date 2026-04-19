from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from l5r_auto.ai.policy import (
    KIND_ACTION_ROUND,
    KIND_ATTACH_TARGET,
    KIND_ATTACK_TARGET,
    KIND_DISCARD_HAND,
    KIND_PAY_GOLD,
    PASS,
    Decision,
    Option,
)

if TYPE_CHECKING:
    from l5r_auto.play import Game


def _force(entity) -> int:
    val = getattr(entity, "force", 0)
    try:
        return int(val)
    except (TypeError, ValueError):
        return 0


def _gold_cost(entity) -> int:
    val = getattr(entity, "gold_cost", 0)
    try:
        return int(val)
    except (TypeError, ValueError):
        return 0


def _gold_production(entity) -> int:
    val = getattr(entity, "gold_production", 0)
    try:
        return int(val)
    except (TypeError, ValueError):
        return 0


# Priority when picking among abilities in an action round.
# Lower number = higher priority.
_ABILITY_PRIORITY = {
    "RecruitAction": 0,
    "PlayStrategyAbility": 1,
    "AttachFollowerAbility": 2,
    "AttachItemAbility": 3,
    "KharmicAction": 4,
    "CycleAction": 5,
}


@dataclass
class HeuristicPolicy:
    """Rule-based policy — the first real AI.

    The goals are modest: beat :class:`RandomPolicy` in self-play so the
    Policy interface is demonstrably useful. Kept intentionally simple; a
    future MCTS/neural policy will replace it, not extend it.
    """

    name: str = "heuristic"
    aggressive: bool = True

    def choose(self, decision: Decision, game: Game) -> list[Option]:
        if not decision.options:
            return []

        kind = decision.kind
        if kind == KIND_ACTION_ROUND:
            return [self._pick_action(decision)]
        if kind == KIND_ATTACK_TARGET:
            return [self._pick_attack(decision, game)]
        if kind == KIND_PAY_GOLD:
            return [self._pick_gold(decision)]
        if kind == KIND_ATTACH_TARGET:
            return [self._pick_attach_target(decision)]
        if kind == KIND_DISCARD_HAND:
            return self._pick_discards(decision)

        # Unknown decision — fall back to first option.
        return [decision.options[0]]

    # --- Action round ---------------------------------------------------

    def _pick_action(self, decision: Decision) -> Option:
        # Rank actions: prefer high-value recruits, then Strategy, then
        # attaches, then cycling. PASS is last resort.
        def rank(opt: Option):
            if opt is PASS or opt.payload is None:
                return (99, 0)
            ability, entity = opt.payload
            cls = ability.__class__.__name__
            prio = _ABILITY_PRIORITY.get(cls, 50)
            # Within an ability class, prefer higher-force / higher-gold-cost
            # targets (proxy for "better card").
            score = -(_force(entity) * 10 + _gold_cost(entity))
            return (prio, score)

        best = min(decision.options, key=rank)
        # Only return PASS if there are no real actions.
        if best is PASS and any(o is not PASS for o in decision.options):
            real = [o for o in decision.options if o is not PASS]
            return min(real, key=rank)
        return best

    # --- Attack target --------------------------------------------------

    def _pick_attack(self, decision: Decision, game: Game) -> Option:
        from l5r_auto.cards.personalities.common import PersonalityEntity

        attacker = decision.player
        defender = decision.context.get("defender")

        # If defender has more unbowed force than we do, declining is safer.
        def unbowed_force(player) -> int:
            return sum(
                _force(e)
                for e in getattr(player, "play_area", [])
                if isinstance(e, PersonalityEntity)
                and getattr(e, "face_up", False)
                and not getattr(e, "bowed", False)
            )

        if defender is not None and not self.aggressive:
            if unbowed_force(attacker) <= unbowed_force(defender):
                return PASS if PASS in decision.options else decision.options[0]

        # Pick the province whose visible face-up force is lowest — the
        # softest target.
        def province_force(opt: Option) -> int:
            if opt is PASS or opt.payload is None:
                return 10**9  # never prefer PASS here
            prov = opt.payload
            return sum(_force(c) for c in getattr(prov, "dynasty_cards", []))

        real = [o for o in decision.options if o is not PASS and o.payload is not None]
        if not real:
            return PASS
        return min(real, key=province_force)

    # --- Gold payment ---------------------------------------------------

    def _pick_gold(self, decision: Decision) -> Option:
        # Bow the smallest producer that still makes progress. Keeps big
        # holdings free for later turns.
        remaining = decision.context.get("remaining_cost", 1)

        def key(opt: Option):
            prod = _gold_production(opt.payload)
            # Smallest producer that covers the remaining cost wins; otherwise
            # the largest available producer.
            covers = prod >= remaining
            return (0 if covers else 1, prod if covers else -prod)

        return min(decision.options, key=key)

    # --- Attach target --------------------------------------------------

    def _pick_attach_target(self, decision: Decision) -> Option:
        # Reinforce the strongest personality that has no attachment yet.
        def key(opt: Option):
            p = opt.payload
            has_attachment = any(
                getattr(e, "attached_to", None) is p
                for e in getattr(p, "owner", None).play_area
            ) if getattr(p, "owner", None) else False
            return (1 if has_attachment else 0, -_force(p))

        return min(decision.options, key=key)

    # --- Discard --------------------------------------------------------

    def _pick_discards(self, decision: Decision) -> list[Option]:
        # Drop cheapest / weakest cards first (low force, low gold_cost).
        def weakness(opt: Option) -> int:
            c = opt.payload
            return _force(c) * 10 + _gold_cost(c)

        ordered = sorted(decision.options, key=weakness)
        n = decision.min_picks
        return ordered[:n]
