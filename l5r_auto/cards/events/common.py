from __future__ import annotations

from typing import Type

from l5r_auto.cards import DynastyCard, Entity
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.utils import dataclass_ as dataclass


@dataclass
class Event(DynastyCard):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = EventEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class EventEntity(Entity, Event):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Event]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Event) if legality in x.legality]
