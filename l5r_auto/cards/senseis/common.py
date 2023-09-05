"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from typing import Type

from l5r_auto.cards import Entity
from l5r_auto.cards.strongholds.common import StrongholdStats
from l5r_auto.clans import Clan
from l5r_auto.legality import Legality
from l5r_auto.locations import Location, StrongholdLocation
from l5r_auto.utils import dataclass_ as dataclass


@dataclass
class Sensei(StrongholdStats):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = SenseiEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class SenseiEntity(Entity, StrongholdStats):
    location: Type[Location] = StrongholdLocation


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Sensei]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Sensei) if legality in x.legality and clan in x.clan]
