from __future__ import annotations

from dataclasses import field
from typing import Type

from l5r_auto.cards import DynastyCard, Entity
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.utils import dataclass_ as dataclass


@dataclass
class Holding(DynastyCard):
    gold_cost: int = field(metadata={"is_written": True})
    gold_production: str | None = field(metadata={"is_written": True})

    def __post_init__(self, *args, **kwargs):
        self.entity_type = HoldingEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class HoldingEntity(Entity, Holding):
    location: Type[Location] = Deck

    def __post_init__(self, *args, **kwargs):
        super().__post_init__(*args, **kwargs)


def get_cards(legality: Type[Legality]) -> list[Holding]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Holding) if legality in x.legality]
