from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Type


@dataclass(kw_only=True)
class Action:
    pass


@dataclass(kw_only=True)
class Ability(Action):
    repeatable: bool = False
    tireless: bool = False
    battle: bool = False


@dataclass(kw_only=True)
class Trait(Action):
    pass


@dataclass(kw_only=True)
class Card:
    id: int


@dataclass(kw_only=True)
class Keyword:
    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.__class__.__name__
