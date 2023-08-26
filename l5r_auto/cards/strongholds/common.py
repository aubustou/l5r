"""Stronghold cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from l5r_auto.card import Card, Keyword
from l5r_auto.card import Ability, Trait
from l5r_auto.clans import Clan
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Stronghold(Card):
    title: str
    province_strength: int
    gold_production: int
    starting_honor: int
    clan: type[Clan]
    keywords: list[Keyword] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    abilities: list[Ability] = field(default_factory=list)


@dataclass(kw_only=True)
class StrongholdEntity(Entity):
    location: str = "battlefield"
