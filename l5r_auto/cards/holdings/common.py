from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, DynastyCard, Keyword, Trait
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Holding(DynastyCard):
    title: str = field(metadata={"is_written": True})
    cost: int = field(metadata={"is_written": True})
    gold_production: int = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = HoldingEntity


@dataclass(kw_only=True)
class HoldingEntity(Entity, Holding):
    location: Type[Location] = Deck
