"""Personality cards from Legend of the Five Rings."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Type

from l5r_auto.cards import DynastyCard, Entity, log_state_change
from l5r_auto.clans import Clan
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location


@dataclass(repr=False, kw_only=True)
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


@dataclass(repr=False, kw_only=True)
class PersonalityEntity(Entity, Personality):
    location: Type[Location] = Deck
    base_card: Type[Personality]

    # States
    dishonored: bool = False

    @log_state_change
    def dishonor(self):
        self.dishonored = True
        self.personal_honor = 0
        self.check_chi_death()

    @log_state_change
    def rehonor(self):
        self.dishonored = False
        self.personal_honor = self.base_card.personal_honor

    def check_chi_death(self):
        """Chi Death Rule: If a Personality's Chi is ever zero, destroy him immediately."""
        if self.chi <= 0:
            logging.info(
                "%s: %s destroyed by Chi Death Rule (Chi=%d).",
                self.owner.name,
                self.title,
                self.chi,
            )
            self.destroy()

    @log_state_change
    def destroy(self):
        """Override Entity.destroy to handle dishonorable death honor loss."""
        from l5r_auto.keywords import Expendable

        # Dishonorable death: controller loses Honor equal to printed Personal Honor
        if self.dishonored:
            printed_ph = self.base_card.personal_honor
            logging.info(
                "%s: %s destroyed while dishonorable — loses %d Honor.",
                self.owner.name,
                self.title,
                printed_ph,
            )
            self.owner.honor -= printed_ph

        # Attachments are discarded when their host is destroyed
        for attached in [
            e for e in self.owner.play_area if getattr(e, "attached_to", None) is self
        ]:
            logging.info(
                "%s: %s discarded with %s.",
                self.owner.name,
                attached.title,
                self.title,
            )
            attached.discard()

        has_expendable = any(
            (isinstance(kw, type) and issubclass(kw, Expendable)) or kw is Expendable
            for kw in self.keywords
        )
        self.bowed = False

        from l5r_auto.locations import DynastyDiscard

        self.move_to(DynastyDiscard)

        if has_expendable:
            logging.debug(
                "%s: %s has Expendable — drawing a fate card.",
                self.owner.name,
                self.title,
            )
            from l5r_auto.errors import EndOfFateDeckError

            try:
                self.owner.draw_fate_card()
            except EndOfFateDeckError:
                pass


def get_cards(legality: Type[Legality], clan: Type[Clan]) -> list[Personality]:
    from .. import get_cards as get_cards_

    return [
        x for x in get_cards_(Personality) if legality in x.legality and clan in x.clan
    ]
