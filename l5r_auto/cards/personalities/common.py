"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from l5r_auto.card import Card
from l5r_auto.card import Ability, Trait
from l5r_auto.player import Entity


@dataclass
class Personality(Card):
    title: str
    force: int
    chi: int
    honor_requirement: int | None
    personal_honor: int
    gold_cost: int
    clan: str
    keywords: list[str] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    abilities: list[Ability] = field(default_factory=list)


@dataclass
class PersonalityEntity(Entity):
    location: str = "deck"
