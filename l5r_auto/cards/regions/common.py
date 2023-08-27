"""Region cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Card, DynastyCard, Keyword
from l5r_auto.card import Ability, Trait
from copy import copy
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity
from l5r_auto.clans import Clan


@dataclass(kw_only=True)
class Region(DynastyCard):
    title: str = field(metadata={"is_written": True})
    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )


@dataclass(kw_only=True)
class RegionEntity(Entity, Region):
    location: Type[Location] = Deck
