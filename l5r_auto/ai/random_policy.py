from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.ai.policy import KIND_PAY_GOLD, Decision, Option

if TYPE_CHECKING:
    from l5r_auto.play import Game


@dataclass
class RandomPolicy:
    """Baseline policy that makes uniform-random choices.

    Preserves the pre-refactor simulation behaviour: every decision picks a
    random legal option. Accepts an optional seeded :class:`random.Random`
    for reproducibility (required for MCTS debugging later).
    """

    name: str = "random"
    rng: random.Random = field(default_factory=random.Random)

    def choose(self, decision: Decision, game: Game) -> list[Option]:
        if not decision.options:
            return []

        # pay_gold is a single-option-per-call decision: the engine calls us
        # repeatedly until the cost is covered. A uniform pick over
        # remaining producers mirrors the old random payment order.
        if decision.kind == KIND_PAY_GOLD:
            return [self.rng.choice(decision.options)]

        n = self.rng.randint(decision.min_picks, decision.max_picks)
        n = min(n, len(decision.options))
        if n <= 0:
            return []
        return self.rng.sample(decision.options, n)
