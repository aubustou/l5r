from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, DynastyCard, Keyword, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity
from l5r_auto.utils import import_submodules

EVENTS: list[Event] = []


@dataclass(kw_only=True)
class Event(DynastyCard):
    title: str = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = EventEntity
        EVENTS.append(self)

        super().__post_init__()


@dataclass(kw_only=True)
class EventEntity(Entity, Event):
    location: Type[Location] = Deck


def get_events(legality: Type[Legality]) -> list[Event]:
    import_submodules(f"l5r_auto.cards.events")
    return [x for x in EVENTS if legality in x.legality]
