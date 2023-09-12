from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Generator

from .locations import PlayArea, ProvinceLocation
from .utils import is_entity_of_type

if TYPE_CHECKING:
    from .cards import Entity, HoldingEntity, PersonalityEntity
    from .play import Game
    from .player import Player

ABILITIES: dict[uuid.UUID, Ability] = {}


@dataclass(repr=False, kw_only=True)
class Action:
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(repr=False, kw_only=True)
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

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def get_effect(self, *args, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def pay_cost(self, game: Game, entity: PersonalityEntity | HoldingEntity) -> bool:
        raise NotImplementedError(f"{self.__class__.__name__} is not implemented.")

    def on_start_phase(self, game: Game):
        self.done_once_per_turn = False

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        return 0


@dataclass(repr=False, kw_only=True)
class Trait(Action):
    pass


@dataclass(repr=False, kw_only=True)
class ProduceGold(Ability):
    """Bow: Produce X Gold."""

    base_gold_amount: str | int = 0

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        return int(self.base_gold_amount)


@dataclass(repr=False, kw_only=True)
class RecruitAction(Ability):
    """Repeatable Dynasty, : Bring into play a target face-up Personality or Holding from
    your Province with Gold Cost equal to the amount you paid, paying 2 more Gold if the
    Personality has a Clan Alignment but does not have your Clan Alignment.
    """

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        for entity in game.entities:
            if (
                entity.owner == active_player
                and entity.location is ProvinceLocation
                and entity.face_up
            ):
                yield entity

    def pay_cost(self, game: Game, entity: PersonalityEntity | HoldingEntity) -> bool:
        gold_cost = entity.gold_cost

        if hasattr(entity, "clan") and entity.owner.clan not in entity.clan:
            # Management of out-of-clan personalities and unaligned personalities
            gold_cost += 2

        gold_producing_entities = [
            x for x in game.current_player.entities if x.can_produce
        ]
        gold_producing_entities.sort(key=lambda x: x.gold_production, reverse=True)

        produced_gold = 0
        bowed_entities = []
        try:
            while produced_gold < gold_cost:
                if not gold_producing_entities:
                    raise ValueError("Not enough gold to pay cost.")
                gold_producing_entity = gold_producing_entities.pop()
                produced_gold += sum(
                    gold_producing_entity.on_pay(game, entity.owner, entity)
                )
                bowed_entities.append(gold_producing_entity)
        except ValueError:
            logging.info(
                "%s: Not enough gold to pay cost (%s) of %s.",
                game.current_player.name,
                gold_cost,
                entity,
            )
            return False
        else:
            logging.info(
                "%s: Paying %d gold for %s.",
                game.current_player.name,
                produced_gold,
                entity,
            )
            for gold_producing_entity in bowed_entities:
                gold_producing_entity.bow()
            return True

    def _recruit_personality(self, game: Game, personality: PersonalityEntity):
        logging.info(
            "%s: Recruiting personality %s into play.",
            personality.owner.name,
            personality,
        )
        personality.move_to(PlayArea)

    def _recruit_holding(self, game: Game, holding: HoldingEntity):
        logging.info(
            "%s: Recruiting holding %s into play.", holding.owner.name, holding
        )
        holding.move_to(PlayArea)
        holding.bow()

    def get_effect(self, game: Game, entity: PersonalityEntity | HoldingEntity):
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


@dataclass(repr=False, kw_only=True)
class ProclaimAction(Ability):
    """Once during your own turn, after
    you announce a Recruit action or an
    action with Recruit as an effect, you
    may choose to Proclaim the Personal-
    ity being recruited. If he has your Clan
    Alignment and is coming from your
    Province, add his Personal Honor to
    your Family Honor after he enters play."""

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
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


@dataclass(repr=False, kw_only=True)
class DynastyDiscardAction(Ability):
    """Repeatable Dynasty: Discard a face-up card from one of your Provinces."""

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        for province in active_player.provinces:
            for card in province.dynasty_cards:
                if card.face_up:
                    yield card

    def pay_cost(self, game: Game, entity: Entity) -> bool:
        return True

    def get_effect(self, game: Game, card: Entity):
        logging.info("%s: Discarding %s.", game.current_player, card)
        card.discard()
