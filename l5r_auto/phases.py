from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


@dataclass(kw_only=True)
class Step:
    pass


@dataclass(kw_only=True)
class Start(Step):
    pass


@dataclass(kw_only=True)
class Turn(Step):
    number: int


@dataclass(kw_only=True)
class Phase(Step):
    turn: Turn
    active_player: Player


@dataclass(kw_only=True)
class ActionPhase(Phase):
    pass


@dataclass(kw_only=True)
class DynastyPhase(Phase):
    pass


@dataclass(kw_only=True)
class AttackPhase(Phase):
    optional: bool = field(default=True, init=False)
    current_segment: AttackPhaseSegment | None = field(default=None, init=False)


# Attack phase
@dataclass(kw_only=True)
class AttackPhaseSegment(Phase):
    pass


@dataclass(kw_only=True)
class Declaration(AttackPhaseSegment):
    pass


@dataclass(kw_only=True)
class Maneuver(AttackPhaseSegment):
    pass


@dataclass(kw_only=True)
class Fight(AttackPhaseSegment):
    pass


# Battles
@dataclass(kw_only=True)
class BattlePhase(Phase):
    pass


@dataclass(kw_only=True)
class EngageSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class CombatSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class ResolutionSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class AftermathSegment(BattlePhase):
    pass
