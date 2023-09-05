"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from typing import Type

from l5r_auto.cards import Entity, FateCard
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.utils import dataclass_ as dataclass


@dataclass
class Strategy(FateCard):
    def __post_init__(self, *args, **kwargs):
        self.entity_type = StrategyEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class StrategyEntity(Entity, Strategy):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Strategy]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Strategy) if legality in x.legality]
