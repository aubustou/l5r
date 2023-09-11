"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

from dataclasses import field
from typing import Type

from l5r_auto.abilities import Ability
from l5r_auto.cards import DynastyCard, Entity, log_state_change
from l5r_auto.clans import Clan
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location
from l5r_auto.utils import dataclass_ as dataclass


class HasZeroChi(Ability):
    def has_zero_chi(self, personality: PersonalityEntity):
        if personality.chi == 0:
            personality.destroy()


@dataclass
class Personality(DynastyCard):
    force: int = field(metadata={"is_written": True})
    chi: int = field(metadata={"is_written": True})
    honor_requirement: int | None = field(metadata={"is_written": True})
    personal_honor: int = field(metadata={"is_written": True})
    gold_cost: int = field(metadata={"is_written": True})
    clan: list[Type[Clan]] = field(metadata={"is_written": True})

    def __post_init__(self, *args, **kwargs):
        self.entity_type = PersonalityEntity

        super().__post_init__(*args, **kwargs)


@dataclass
class PersonalityEntity(Entity, Personality):
    location: Type[Location] = Deck
    base_card: Type[Personality]

    # States
    dishonored: bool = False

    @log_state_change
    def dishonor(self):
        self.dishonored = True
        self.personal_honor = 0

    @log_state_change
    def rehonor(self):
        self.dishonored = False
        self.personal_honor = self.base_card.personal_honor


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Personality]:
    from .. import get_cards as get_cards_

    return [
        x for x in get_cards_(Personality) if legality in x.legality and clan in x.clan
    ]
