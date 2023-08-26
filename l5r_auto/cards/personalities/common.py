"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Card, Keyword
from l5r_auto.card import Ability, Trait
from copy import copy
from l5r_auto.player import Entity


def SoulOf(title: str) -> Type[Keyword]:
    klass = copy(Keyword)
    klass.name = f"Soul of {title}"

    return klass


@dataclass(kw_only=True)
class Personality(Card):
    title: str
    force: int
    chi: int
    honor_requirement: int | None
    personal_honor: int
    gold_cost: int
    clan: str
    keywords: list[Type[Keyword]] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    abilities: list[Ability] = field(default_factory=list)


@dataclass(kw_only=True)
class PersonalityEntity(Entity):
    location: str = "deck"
