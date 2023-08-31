"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Card, FateCard, Keyword
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Strategy(FateCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = StrategyEntity


@dataclass(kw_only=True)
class StrategyEntity(Entity, Strategy):
    location: Type[Location] = Deck