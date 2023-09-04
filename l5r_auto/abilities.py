from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.locations import PlayArea
from l5r_auto.utils import is_entity_of_type

if TYPE_CHECKING:
    from .cards.holdings.common import HoldingEntity
    from .cards.personalities.common import PersonalityEntity
    from .play import Game


@dataclass(kw_only=True)
class Action:
    pass


@dataclass(kw_only=True)
class Ability(Action):
    repeatable: bool = field(default=False, init=False)
    tireless: bool = field(default=False, init=False)

    battle: bool = field(default=False, init=False)
    limited: bool = field(default=False, init=False)
    open: bool = field(default=False, init=False)
    interrupt: bool = field(default=False, init=False)
    dynasty: bool = field(default=False, init=False)


@dataclass(kw_only=True)
class Trait(Action):
    pass


@dataclass(kw_only=True)
class RecruitAction(Ability):
    """Repeatable Dynasty, : Bring into play a target face-up Personality or Holding from
    your Province with Gold Cost equal to the amount you paid, paying 2 more Gold if the
    Personality has a Clan Alignment but does not have your Clan Alignment.
    """

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def _recruit_personality(self, game: Game, personality: PersonalityEntity):
        logging.info(
            "%s: Recruiting personality %s into play.", personality.owner, personality
        )
        personality.location = PlayArea

    def _recruit_holding(self, game: Game, holding: HoldingEntity):
        logging.info("Recruiting holding %s into play.", holding)
        holding.location = PlayArea
        holding.bow()

    def do(self, game: Game, entity: PersonalityEntity | HoldingEntity):
        if is_entity_of_type(entity, PersonalityEntity):
            self._recruit_personality(game, entity)
        elif is_entity_of_type(entity, HoldingEntity):
            self._recruit_holding(game, entity)
        else:
            raise TypeError(f"Cannot recruit {entity}.")


@dataclass(kw_only=True)
class ProclaimAction(Ability):
    """Once during your own turn, after
    you announce a Recruit action or an
    action with Recruit as an effect, you
    may choose to Proclaim the Personal-
    ity being recruited. If he has your Clan
    Alignment and is coming from your
    Province, add his Personal Honor to
    your Family Honor after he enters play."""

    def on_recruit(self, game: Game, personality: PersonalityEntity):
        if personality.owner == game.current_player:
            logging.info(
                "%s: Proclaiming personality %s into play.",
                personality.owner,
                personality,
            )
            personality.owner.honor += personality.personal_honor


@dataclass(kw_only=True)
class DynastyDiscardAction(Ability):
    """Repeatable Dynasty: Discard a face-up card from one of your Provinces."""

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def do(self, game: Game, card: PersonalityEntity | HoldingEntity):
        logging.info("%s: Discarding %s.", game.current_player, card)
        card.discard()
