"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from l5r_auto.card import Entity, FateCard
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location


@dataclass(kw_only=True)
class Spell(FateCard):
    def __post_init__(self):
        self.entity_type = SpellEntity

        super().__post_init__()


@dataclass(kw_only=True)
class SpellEntity(Entity, Spell):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Spell]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Spell) if legality in x.legality]
