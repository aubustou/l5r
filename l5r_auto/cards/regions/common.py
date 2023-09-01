"""Region cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, DynastyCard, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Region(DynastyCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = RegionEntity

        super().__post_init__()


@dataclass(kw_only=True)
class RegionEntity(Entity, Region):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Region]:
    from .. import CARDS

    return [x for x in CARDS.get(Region, {}).values() if legality in x.legality]
