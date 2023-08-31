"""Region cards from Legend of the Five Rings."""

from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, Card, DynastyCard, Keyword, Trait
from l5r_auto.clans import Clan
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Region(DynastyCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )


@dataclass(kw_only=True)
class RegionEntity(Entity, Region):
    location: Type[Location] = Deck
