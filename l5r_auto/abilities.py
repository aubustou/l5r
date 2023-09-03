from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Action:
    pass


@dataclass(kw_only=True)
class Ability(Action):
    repeatable: bool = False
    tireless: bool = False
    battle: bool = False
    limited: bool = False
    open: bool = False
    interrupt: bool = False


@dataclass(kw_only=True)
class Trait(Action):
    pass
