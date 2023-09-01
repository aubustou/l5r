"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, FateCard, Trait
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Follower(FateCard):
    force: str = field(metadata={"is_written": True})
    chi: str = field(metadata={"is_written": True})
    honor_requirement: int | None = field(metadata={"is_written": True})
    personal_honor: int = field(metadata={"is_written": True})

    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = FollowerEntity

        super().__post_init__()


@dataclass(kw_only=True)
class FollowerEntity(Entity, Follower):
    location: Type[Location] = Deck
    attached_to: PersonalityEntity | None = None
