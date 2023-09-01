from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, DynastyCard, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity

HOLDINGS: list[Holding] = []


@dataclass(kw_only=True)
class Holding(DynastyCard):
    title: str = field(metadata={"is_written": True})
    gold_cost: int = field(metadata={"is_written": True})
    gold_production: str | None = field(default=None, metadata={"is_written": True})

    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = HoldingEntity
        HOLDINGS.append(self)

        super().__post_init__()


@dataclass(kw_only=True)
class HoldingEntity(Entity, Holding):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Holding]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Holding) if legality in x.legality]
