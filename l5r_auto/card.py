from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Type


@dataclass
class Action:
    pass


@dataclass
class Ability(Action):
    repeatable: bool = False
    tireless: bool = False
    battle: bool = False


@dataclass
class Trait(Action):
    pass


@dataclass
class Card:
    id: int
