"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, FateCard, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Ring(FateCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = RingEntity

        super().__post_init__()


@dataclass(kw_only=True)
class RingEntity(Entity, Ring):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Ring]:
    from .. import CARDS

    return [x for x in CARDS.get(Ring, {}).values() if legality in x.legality]
