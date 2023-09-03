from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from l5r_auto.card import DynastyCard, Entity
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location

EVENTS: list[Event] = []


@dataclass(kw_only=True)
class Event(DynastyCard):
    def __post_init__(self):
        self.entity_type = EventEntity
        EVENTS.append(self)

        super().__post_init__()


@dataclass(kw_only=True)
class EventEntity(Entity, Event):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Event]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Event) if legality in x.legality]
