"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Card, DynastyCard, Keyword
from l5r_auto.card import Ability, Trait
from copy import copy
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity
from l5r_auto.clans import Clan


def SoulOf(title: str) -> Type[Keyword]:
    klass = copy(Keyword)
    klass.name = f"Soul of {title}"

    return klass


class HasZeroChi(Ability):
    def has_zero_chi(self, personality: PersonalityEntity):
        if personality.chi == 0:
            personality.destroy()


@dataclass(kw_only=True)
class Personality(DynastyCard):
    title: str = field(metadata={"is_written": True})
    force: int = field(metadata={"is_written": True})
    chi: int = field(metadata={"is_written": True})
    honor_requirement: int | None = field(metadata={"is_written": True})
    personal_honor: int = field(metadata={"is_written": True})
    gold_cost: int = field(metadata={"is_written": True})
    clan: list[Type[Clan]] = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = PersonalityEntity


@dataclass(kw_only=True)
class PersonalityEntity(Entity, Personality):
    location: Type[Location] = Deck

    def bow(self):
        self.bowed = True
