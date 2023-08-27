"""Stronghold cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Card, Keyword
from l5r_auto.card import Ability, Trait
from l5r_auto.clans import Clan
from l5r_auto.locations import Location, Stronghold as StrongholdLocation
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Stronghold(Card):
    title: str = field(metadata={"is_written": True})
    province_strength: int = field(metadata={"is_written": True})
    gold_production: int = field(metadata={"is_written": True})
    starting_family_honor: int = field(metadata={"is_written": True})
    clan: type[Clan] = field(metadata={"is_written": True})
    keywords: list[Keyword] = field(default_factory=list, metadata={"is_written": True})
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = StrongholdEntity


@dataclass(kw_only=True)
class StrongholdEntity(Entity, Stronghold):
    location: Type[Location] = StrongholdLocation
