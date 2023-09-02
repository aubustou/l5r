"""Stronghold cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Type

from l5r_auto.card import Ability, Card, Entity, Trait
from l5r_auto.locations import Stronghold as StrongholdLocation

if TYPE_CHECKING:
    from l5r_auto.clans import Clan
    from l5r_auto.legality import Legality
    from l5r_auto.locations import Location


@dataclass(kw_only=True)
class StrongholdStats(Card):
    province_strength: int = field(metadata={"is_written": True})
    gold_production: str = field(metadata={"is_written": True})
    starting_family_honor: int = field(metadata={"is_written": True})
    clan: list[type[Clan]] = field(metadata={"is_written": True})
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )


@dataclass(kw_only=True)
class Stronghold(StrongholdStats):
    def __post_init__(self):
        self.entity_type = StrongholdEntity

        super().__post_init__()


@dataclass(kw_only=True)
class StrongholdEntity(Entity, StrongholdStats):
    location: Type[Location] = StrongholdLocation


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Stronghold]:
    from .. import get_cards as get_cards_

    return [
        x for x in get_cards_(Stronghold) if legality in x.legality and clan in x.clan
    ]
