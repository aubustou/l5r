"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import field
from typing import Type

from l5r_auto.cards import Entity, FateCard
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.utils import dataclass_ as dataclass

from ..personalities.common import PersonalityEntity


@dataclass
class Follower(FateCard):
    force: str = field(metadata={"is_written": True})
    chi: str = field(metadata={"is_written": True})
    honor_requirement: int | None = field(metadata={"is_written": True})
    personal_honor: int = field(metadata={"is_written": True})

    def __post_init__(self, *args, **kwargs):
        self.entity_type = FollowerEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class FollowerEntity(Entity, Follower):
    location: Type[Location] = Deck
    attached_to: PersonalityEntity | None = None


def get_cards(legality: Type[Legality]) -> list[Follower]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Follower) if legality in x.legality]
