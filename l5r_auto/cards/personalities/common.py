"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type

from l5r_auto.card import Ability, DynastyCard, Trait
from l5r_auto.clans import Clan
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.player import Entity


class HasZeroChi(Ability):
    def has_zero_chi(self, personality: PersonalityEntity):
        if personality.chi == 0:
            personality.destroy()


PERSONALITIES: list[Personality] = []


@dataclass(kw_only=True)
class Personality(DynastyCard):
    force: int = field(metadata={"is_written": True})
    chi: int = field(metadata={"is_written": True})
    honor_requirement: int | None = field(metadata={"is_written": True})
    personal_honor: int = field(metadata={"is_written": True})
    gold_cost: int = field(metadata={"is_written": True})
    clan: list[Type[Clan]] = field(metadata={"is_written": True})

    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

    def __post_init__(self):
        self.entity_type = PersonalityEntity
        PERSONALITIES.append(self)

        super().__post_init__()


@dataclass(kw_only=True)
class PersonalityEntity(Entity, Personality):
    location: Type[Location] = Deck

    def bow(self):
        self.bowed = True


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Personality]:
    from .. import CARDS

    return [
        x
        for x in CARDS.get(Personality, {}).values()
        if legality in x.legality and clan in x.clan
    ]
