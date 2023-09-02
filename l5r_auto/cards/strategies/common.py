"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, Entity, FateCard, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location


@dataclass(kw_only=True)
class Strategy(FateCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = StrategyEntity

        super().__post_init__()


@dataclass(kw_only=True)
class StrategyEntity(Entity, Strategy):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Strategy]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Strategy) if legality in x.legality]
