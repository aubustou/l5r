"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from l5r_auto.cards import Entity, FateCard
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location


@dataclass(kw_only=True)
class Ring(FateCard):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = RingEntity

        super().__post_init__(*args, **kwargs)


@dataclass(kw_only=True)
class RingEntity(Entity, Ring):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Ring]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Ring) if legality in x.legality]
