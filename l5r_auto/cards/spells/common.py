"""Follower cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, FateCard, Trait
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


@dataclass(kw_only=True)
class Spell(FateCard):
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = SpellEntity

        super().__post_init__()


@dataclass(kw_only=True)
class SpellEntity(Entity, Spell):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Spell]:
    from .. import CARDS

    return [x for x in CARDS.get(Spell, {}).values() if legality in x.legality]
