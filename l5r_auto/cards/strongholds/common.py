"""Stronghold cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Type

from l5r_auto.cards import Card, Entity
from l5r_auto.cards.holdings.common import ProduceGold
from l5r_auto.locations import StrongholdLocation

if TYPE_CHECKING:
    from l5r_auto.clans import Clan
    from l5r_auto.legality import Legality
    from l5r_auto.locations import Location


@dataclass(repr=False, kw_only=True)
class StrongholdStats(Card):
    province_strength: int = field(metadata={"is_written": True})
    gold_production: str = field(metadata={"is_written": True})
    starting_family_honor: int = field(metadata={"is_written": True})
    clan: list[type[Clan]] = field(metadata={"is_written": True})


@dataclass(repr=False, kw_only=True)
class Stronghold(StrongholdStats):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = StrongholdEntity

        if not any(isinstance(x, ProduceGold) for x in self.abilities):
            self.abilities.append(ProduceGold(base_gold_amount=self.gold_production))

        super().__post_init__(*args, **kwargs)


@dataclass(repr=False, kw_only=True)
class StrongholdEntity(Entity, StrongholdStats):
    location: Type[Location] = StrongholdLocation


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Stronghold]:
    from .. import get_cards as get_cards_

    return [
        x for x in get_cards_(Stronghold) if legality in x.legality and clan in x.clan
    ]
