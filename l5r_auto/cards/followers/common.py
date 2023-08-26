"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from l5r_auto.card import Card
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.player import Entity


@dataclass
class Follower(Card):
    title: str
    force: str
    chi: str
    honor_requirement: int | None
    gold_cost: int
    personal_honor: int
    focus_value: int
    keywords: list[str] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    abilities: list[Ability] = field(default_factory=list)


@dataclass
class FollowerEntity(Entity):
    location: str = "deck"
    attached_to: PersonalityEntity | None = None
