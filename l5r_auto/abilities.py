from __future__ import annotations

import logging
import uuid
from dataclasses import field
from typing import TYPE_CHECKING, Generator

from l5r_auto.utils import dataclass_ as dataclass

from .locations import PlayArea, ProvinceLocation
from .utils import is_entity_of_type

if TYPE_CHECKING:
    from .cards import Entity, HoldingEntity, PersonalityEntity
    from .play import Game
    from .player import Player

ABILITIES: dict[uuid.UUID, Ability] = {}


@dataclass
class Action:
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Ability(Action):
    repeatable: bool = field(default=False, init=False)
    tireless: bool = field(default=False, init=False)

    battle: bool = field(default=False, init=False)
    limited: bool = field(default=False, init=False)
    open: bool = field(default=False, init=False)
    interrupt: bool = field(default=False, init=False)
    dynasty: bool = field(default=False, init=False)

    done_once_per_turn: bool = field(default=False, init=False)

    def __post_init__(self, *args, **kwargs):
        ABILITIES[self.id] = self

    def do(self, *args, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def legal(self, game: Game, active_player: Player) -> Generator[Entity, None, None]:
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def on_start_phase(self, game: Game):
        self.done_once_per_turn = False


@dataclass
class Trait(Action):
    pass


@dataclass
class RecruitAction(Ability):
    """Repeatable Dynasty, : Bring into play a target face-up Personality or Holding from
    your Province with Gold Cost equal to the amount you paid, paying 2 more Gold if the
    Personality has a Clan Alignment but does not have your Clan Alignment.
    """

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def legal(self, game: Game, active_player: Player) -> Generator[Entity, None, None]:
        for entity in game.entities:
            if (
                entity.owner == active_player
                and entity.location is ProvinceLocation
                and entity.face_up
            ):
                yield entity

    def _recruit_personality(self, game: Game, personality: PersonalityEntity):
        logging.info(
            "%s: Recruiting personality %s into play.",
            personality.owner.name,
            personality,
        )
        personality.location = PlayArea

    def _recruit_holding(self, game: Game, holding: HoldingEntity):
        logging.info(
            "%s: Recruiting holding %s into play.", holding.owner.name, holding
        )
        holding.location = PlayArea
        holding.bow()

    def do(self, game: Game, entity: PersonalityEntity | HoldingEntity):
        from .cards import HoldingEntity, PersonalityEntity

        province = entity.province

        if is_entity_of_type(entity, PersonalityEntity):
            self._recruit_personality(game, entity)
        elif is_entity_of_type(entity, HoldingEntity):
            self._recruit_holding(game, entity)
        else:
            raise TypeError(f"Cannot recruit {entity.__class__.__name__}.")

        province.dynasty_cards.remove(entity)
        province.fill()


def once_per_turn(method):
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        self.done_once_per_turn = True

    return wrapper


@dataclass
class ProclaimAction(Ability):
    """Once during your own turn, after
    you announce a Recruit action or an
    action with Recruit as an effect, you
    may choose to Proclaim the Personal-
    ity being recruited. If he has your Clan
    Alignment and is coming from your
    Province, add his Personal Honor to
    your Family Honor after he enters play."""

    def legal(self, game: Game, active_player: Player) -> Generator[Entity, None, None]:
        if self.done_once_per_turn:
            raise StopIteration

        for entity in game.entities:
            if entity.owner == active_player:
                yield entity

    @once_per_turn
    def on_recruit(self, game: Game, personality: PersonalityEntity):
        if personality.owner == game.current_player:
            logging.info(
                "%s: Proclaiming personality %s into play.",
                personality.owner,
                personality,
            )
            personality.owner.honor += personality.personal_honor

    def on_start_phase(self, game: Game):
        self.done_once_per_turn = False


@dataclass
class DynastyDiscardAction(Ability):
    """Repeatable Dynasty: Discard a face-up card from one of your Provinces."""

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def legal(self, game: Game, active_player: Player) -> Generator[Entity, None, None]:
        for province in active_player.provinces:
            for card in province.dynasty_cards:
                yield card

    def do(self, game: Game, card: PersonalityEntity | HoldingEntity):
        logging.info("%s: Discarding %s.", game.current_player, card)
        card.discard()
