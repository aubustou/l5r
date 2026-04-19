from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from l5r_auto.play import Game
    from l5r_auto.player import Player


# Well-known decision kinds. Kept as constants so policies and tests can match
# on them without magic strings going stale.
KIND_ATTACK_TARGET = "attack_target"
KIND_ACTION_ROUND = "action_round"
KIND_PAY_GOLD = "pay_gold"
KIND_ATTACH_TARGET = "attach_target"
KIND_DISCARD_HAND = "discard_hand"
KIND_RECRUIT_TARGET = "recruit_target"


@dataclass(frozen=True)
class Option:
    """A single concrete choice presented to a policy.

    ``id`` is a stable string (useful for logging and, later, as an action
    index for training). ``payload`` is the live object (Entity, Province,
    tuple of ability + target, ...) the engine needs to act on.
    """

    id: str
    payload: Any = None

    def __repr__(self) -> str:
        return f"Option({self.id!r})"


PASS = Option(id="PASS", payload=None)


@dataclass
class Decision:
    """A choice point the engine poses to a player's policy."""

    kind: str
    player: Player
    options: list[Option]
    min_picks: int = 1
    max_picks: int = 1
    context: dict = field(default_factory=dict)

    def option_by_id(self, option_id: str) -> Option | None:
        for opt in self.options:
            if opt.id == option_id:
                return opt
        return None


class Policy(Protocol):
    """Anything that can turn a Decision into a set of chosen Options.

    Implementations live in :mod:`l5r_auto.ai.random_policy`,
    :mod:`l5r_auto.ai.heuristic_policy`, and eventually MCTS / neural net.
    """

    name: str

    def choose(self, decision: Decision, game: Game) -> list[Option]: ...
