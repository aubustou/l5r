"""Region cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from l5r_auto.cards import DynastyCard, Entity
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location


@dataclass(repr=False, kw_only=True)
class Region(DynastyCard):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = RegionEntity

        super().__post_init__(*args, **kwargs)


@dataclass(repr=False, kw_only=True)
class RegionEntity(Entity, Region):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Region]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Region) if legality in x.legality]
