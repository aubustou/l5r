from __future__ import annotations

import logging
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Generator

from .locations import Hand, PlayArea, ProvinceLocation
from .utils import is_entity_of_type

if TYPE_CHECKING:
    from .cards import Entity, FateCard, HoldingEntity, PersonalityEntity
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

    def can_pay(self, game: Game, entity: Entity) -> bool:
        """Side-effect-free affordability check.

        Used by :func:`Phase.legal_actions` to enumerate plays without
        mutating state. Defaults to ``True``; override in subclasses whose
        ``gather_legal_target_entities`` does not already pre-filter by cost.
        """
        return True


@dataclass(repr=False, kw_only=True)
class Trait(Action):
    pass


@dataclass(repr=False, kw_only=True)
class ProduceGold(Ability):
    """Bow: Produce X Gold."""

    base_gold_amount: str | int = 0

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        try:
            return int(self.base_gold_amount)
        except (ValueError, TypeError):
            # Handle non-numeric gold amounts like "2*" — use numeric prefix
            raw = str(self.base_gold_amount).rstrip("*+GX")
            try:
                return int(raw) if raw else 0
            except ValueError:
                return 0


@dataclass(repr=False, kw_only=True)
class RecruitAction(Ability):
    """Repeatable Dynasty, : Bring into play a target face-up Personality or Holding from
    your Province with Gold Cost equal to the amount you paid, paying 2 more Gold if the
    Personality has a Clan Alignment but does not have your Clan Alignment.
    """

    repeatable: bool = field(default=True, init=False)
    dynasty: bool = field(default=True, init=False)
    _proclaim_action: Ability | None = field(default=None, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        from .keywords import Loyal, Unique

        titles_in_play = {
            e.title for e in game.entities if e.location is PlayArea and e.face_up
        }

        for entity in game.entities:
            if not (
                entity.owner == active_player
                and entity.location is ProvinceLocation
                and entity.face_up
                and hasattr(entity, "gold_cost")
            ):
                continue
            # Unique: skip if a card with the same title is already in play
            is_unique = any(
                (isinstance(kw, type) and issubclass(kw, Unique)) or kw is Unique
                for kw in entity.keywords
            )
            if is_unique and entity.title in titles_in_play:
                logging.info(
                    "%s: Skipping Unique card %s — already in play.",
                    active_player.name,
                    entity.title,
                )
                continue
            # Loyal: skip if personality is loyal and belongs to a different clan
            is_loyal = any(
                (isinstance(kw, type) and issubclass(kw, Loyal)) or kw is Loyal
                for kw in entity.keywords
            )
            if (
                is_loyal
                and hasattr(entity, "clan")
                and entity.clan
                and active_player.clan not in entity.clan
            ):
                logging.info(
                    "%s: Skipping Loyal card %s — cannot recruit out-of-clan.",
                    active_player.name,
                    entity.title,
                )
                continue
            # Honor Requirement: player's honor must be >= personality's HR
            hr = getattr(entity, "honor_requirement", None)
            if hr is not None and active_player.honor < hr:
                logging.info(
                    "%s: Skipping %s — Honor Requirement %d not met (honor: %d).",
                    active_player.name,
                    entity.title,
                    hr,
                    active_player.honor,
                )
                continue
            yield entity

    def _effective_gold_cost(self, entity: Entity) -> int:
        gold_cost = entity.gold_cost
        if hasattr(entity, "clan") and entity.owner.clan not in entity.clan:
            # Management of out-of-clan personalities and unaligned personalities
            gold_cost += 2
        return gold_cost

    def can_pay(self, game: Game, entity: Entity) -> bool:
        player = entity.owner
        producible = sum(
            sum(e.on_pay(game, player, e)) for e in player.entities if e.can_produce
        )
        return producible >= self._effective_gold_cost(entity)

    def pay_cost(self, game: Game, entity: PersonalityEntity | HoldingEntity) -> bool:
        gold_cost = self._effective_gold_cost(entity)
        result = _pay_gold(game, entity.owner, gold_cost, target=entity)
        if not result:
            logging.info(
                "%s: Not enough gold to pay cost (%s) of %s.",
                game.current_player.name,
                gold_cost,
                entity,
            )
        return result

    def _recruit_personality(self, game: Game, personality: PersonalityEntity):
        logging.info(
            "%s: Recruiting personality %s into play.",
            personality.owner.name,
            personality,
        )
        personality.move_to(PlayArea)

        if self._proclaim_action is not None:
            self._proclaim_action.try_proclaim(game, personality)

    def _recruit_holding(self, game: Game, holding: HoldingEntity):
        logging.info(
            "%s: Recruiting holding %s into play.", holding.owner.name, holding
        )
        holding.move_to(PlayArea)
        holding.bow()

    def _get_experienced_level(self, entity) -> int | None:
        """Return the Experienced level of a card, or None if not Experienced."""
        for kw in entity.keywords:
            if isinstance(kw, type) and hasattr(kw, "level"):
                try:
                    return int(kw.level)
                except (ValueError, TypeError):
                    return 1
        return None

    def _try_overlay_experienced(self, game: Game, entity: PersonalityEntity) -> bool:
        """Attempt to overlay an Experienced personality onto a lower-experience version.

        Returns True if overlay occurred (skip normal recruit), False otherwise.
        """
        from .cards.personalities.common import PersonalityEntity as PE

        new_level = self._get_experienced_level(entity)
        if new_level is None:
            return False

        for existing in entity.owner.play_area:
            if (
                isinstance(existing, PE)
                and existing.title == entity.title
                and (self._get_experienced_level(existing) or 0) < new_level
            ):
                logging.info(
                    "%s: Overlaying Experienced %s (level %d) onto existing (level %d).",
                    entity.owner.name,
                    entity.title,
                    new_level,
                    self._get_experienced_level(existing) or 0,
                )
                # Transfer attachments
                for att in entity.owner.play_area[:]:
                    if getattr(att, "attached_to", None) is existing:
                        att.attached_to = entity
                # Remove old version from play
                existing.remove_from_game()
                # Place new version directly into play
                entity.move_to(PlayArea)
                return True

        return False

    def get_effect(self, game: Game, entity: PersonalityEntity | HoldingEntity):
        from .cards import HoldingEntity, PersonalityEntity

        province = entity.province

        if is_entity_of_type(entity, PersonalityEntity):
            if not self._try_overlay_experienced(game, entity):
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
    """Once per turn, after recruiting a personality whose clan matches your stronghold's clan
    (from your province), you may gain honor equal to that personality's Personal Honor."""

    def try_proclaim(self, game: Game, personality: PersonalityEntity) -> bool:
        """AI always chooses to proclaim when eligible and the once-per-turn limit allows."""
        if self.done_once_per_turn:
            return False
        if not (
            hasattr(personality, "clan") and personality.owner.clan in personality.clan
        ):
            return False
        self.done_once_per_turn = True
        logging.info(
            "%s: Proclaims %s — gains %d Honor.",
            personality.owner.name,
            personality.title,
            personality.personal_honor,
        )
        personality.owner.honor += personality.personal_honor
        return True


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


def _pay_gold(
    game: Game,
    player: Player,
    gold_cost: int,
    target: Entity | None = None,
) -> bool:
    """Bow gold-producing entities owned by player to cover gold_cost.

    The selection is mediated by ``player.policy`` one producer at a time:
    the engine repeatedly asks the policy to pick the next producer to bow
    until the cost is covered. Returns True and bows on success, False (and
    does not bow anything) if insufficient gold is producible.
    """
    from l5r_auto.ai.policy import KIND_PAY_GOLD, Decision, Option

    available = [x for x in player.entities if x.can_produce]

    # Up-front affordability check — side-effect free.
    total_producible = sum(sum(e.on_pay(game, player, e)) for e in available)
    if total_producible < gold_cost:
        logging.info("%s: Not enough gold to pay %d.", player.name, gold_cost)
        return False

    bowed: list[Entity] = []
    produced = 0
    remaining = list(available)
    while produced < gold_cost and remaining:
        options = [
            Option(id=f"bow:{e.id}:{e.title}", payload=e) for e in remaining
        ]
        decision = Decision(
            kind=KIND_PAY_GOLD,
            player=player,
            options=options,
            context={
                "gold_cost": gold_cost,
                "produced": produced,
                "remaining_cost": gold_cost - produced,
                "target": target,
            },
        )
        picked = player.policy.choose(decision, game)
        if not picked:
            # Policy declined to pay — abort without side effects.
            return False
        gpe = picked[0].payload
        remaining.remove(gpe)
        bowed.append(gpe)
        produced += sum(gpe.on_pay(game, player, gpe))

    if produced < gold_cost:
        return False

    logging.info("%s: Paying %d gold.", player.name, produced)
    for gpe in bowed:
        gpe.bow()
    return True


@dataclass(repr=False, kw_only=True)
class PlayStrategyAbility(Ability):
    """Action: Play a Strategy card from your hand by paying its gold cost."""

    open: bool = field(default=True, init=False)
    repeatable: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        from .cards.strategies.common import StrategyEntity

        gold_available = sum(
            sum(e.on_pay(game, active_player, e))
            for e in active_player.entities
            if e.can_produce
        )
        for card in active_player.hand[:]:
            if isinstance(card, StrategyEntity) and card.gold_cost <= gold_available:
                yield card

    def can_pay(self, game: Game, entity: Entity) -> bool:
        player = entity.owner
        producible = sum(
            sum(e.on_pay(game, player, e)) for e in player.entities if e.can_produce
        )
        return producible >= getattr(entity, "gold_cost", 0)

    def pay_cost(self, game: Game, entity: FateCard) -> bool:
        return _pay_gold(game, entity.owner, entity.gold_cost, target=entity)

    def get_effect(self, game: Game, card: Entity):
        from .locations import FateDiscard

        logging.info("%s: Playing strategy %s.", card.owner.name, card.title)
        card.move_to(FateDiscard)


@dataclass(repr=False, kw_only=True)
class AttachFollowerAbility(Ability):
    """Action: Attach a Follower card from hand to a Personality in play."""

    open: bool = field(default=True, init=False)
    repeatable: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        from .cards.followers.common import FollowerEntity
        from .cards.personalities.common import PersonalityEntity

        personalities_in_play = [
            e
            for e in active_player.play_area
            if isinstance(e, PersonalityEntity) and e.face_up
        ]
        if not personalities_in_play:
            return

        gold_available = sum(
            sum(e.on_pay(game, active_player, e))
            for e in active_player.entities
            if e.can_produce
        )
        for card in active_player.hand[:]:
            if isinstance(card, FollowerEntity) and card.gold_cost <= gold_available:
                yield card

    def can_pay(self, game: Game, entity: Entity) -> bool:
        player = entity.owner
        producible = sum(
            sum(e.on_pay(game, player, e)) for e in player.entities if e.can_produce
        )
        return producible >= getattr(entity, "gold_cost", 0)

    def pay_cost(self, game: Game, entity: FateCard) -> bool:
        return _pay_gold(game, entity.owner, entity.gold_cost, target=entity)

    def get_effect(self, game: Game, card: Entity):
        from .ai.policy import KIND_ATTACH_TARGET, Decision, Option
        from .cards.personalities.common import PersonalityEntity

        personalities_in_play = [
            e
            for e in card.owner.play_area
            if isinstance(e, PersonalityEntity) and e.face_up
        ]
        if not personalities_in_play:
            return
        options = [
            Option(id=f"attach:{p.id}:{p.title}", payload=p)
            for p in personalities_in_play
        ]
        decision = Decision(
            kind=KIND_ATTACH_TARGET,
            player=card.owner,
            options=options,
            context={"attachment": card, "attachment_kind": "follower"},
        )
        picked = card.owner.policy.choose(decision, game)
        target = picked[0].payload if picked else personalities_in_play[0]
        logging.info(
            "%s: Attaching follower %s to %s.",
            card.owner.name,
            card.title,
            target.title,
        )
        card.attached_to = target
        card.move_to(PlayArea)


@dataclass(repr=False, kw_only=True)
class AttachItemAbility(Ability):
    """Action: Attach an Item card from hand to a Personality in play."""

    open: bool = field(default=True, init=False)
    repeatable: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        from .cards.items.common import ItemEntity
        from .cards.personalities.common import PersonalityEntity

        personalities_in_play = [
            e
            for e in active_player.play_area
            if isinstance(e, PersonalityEntity) and e.face_up
        ]
        if not personalities_in_play:
            return

        gold_available = sum(
            sum(e.on_pay(game, active_player, e))
            for e in active_player.entities
            if e.can_produce
        )
        for card in active_player.hand[:]:
            if isinstance(card, ItemEntity) and card.gold_cost <= gold_available:
                yield card

    def can_pay(self, game: Game, entity: Entity) -> bool:
        player = entity.owner
        producible = sum(
            sum(e.on_pay(game, player, e)) for e in player.entities if e.can_produce
        )
        return producible >= getattr(entity, "gold_cost", 0)

    def pay_cost(self, game: Game, entity: FateCard) -> bool:
        return _pay_gold(game, entity.owner, entity.gold_cost, target=entity)

    def get_effect(self, game: Game, card: Entity):
        from .ai.policy import KIND_ATTACH_TARGET, Decision, Option
        from .cards.personalities.common import PersonalityEntity

        personalities_in_play = [
            e
            for e in card.owner.play_area
            if isinstance(e, PersonalityEntity) and e.face_up
        ]
        if not personalities_in_play:
            return
        options = [
            Option(id=f"attach:{p.id}:{p.title}", payload=p)
            for p in personalities_in_play
        ]
        decision = Decision(
            kind=KIND_ATTACH_TARGET,
            player=card.owner,
            options=options,
            context={"attachment": card, "attachment_kind": "item"},
        )
        picked = card.owner.policy.choose(decision, game)
        target = picked[0].payload if picked else personalities_in_play[0]
        logging.info(
            "%s: Attaching item %s to %s.",
            card.owner.name,
            card.title,
            target.title,
        )
        card.attached_to = target
        card.move_to(PlayArea)


@dataclass(repr=False, kw_only=True)
class CycleAction(Ability):
    """Limited (first turn only): Choose any number of face-up cards in your Provinces.
    Put them on the bottom of your Dynasty deck, refill the Provinces face-up.
    """

    limited: bool = field(default=True, init=False)
    _first_turn_only: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        # Only available on turn 1 for this player
        if game.current_phase and hasattr(game.current_phase, "turn"):
            if game.current_phase.turn.number > 2:
                # Turn 1 = first player, turn 2 = second player's first turn
                return
        for province in active_player.provinces:
            for card in province.dynasty_cards:
                if card.face_up:
                    yield card

    def pay_cost(self, game: Game, entity: Entity) -> bool:
        return True

    def get_effect(self, game: Game, card: Entity):
        province = card.province
        logging.info(
            "%s: Cycling %s from province to bottom of dynasty deck.",
            card.owner.name,
            card.title,
        )
        province.dynasty_cards.remove(card)
        card.owner.dynasty_deck.insert(0, card)
        from .locations import Deck

        card.location = Deck
        card.turn_face_down()
        province.fill()
        # New card enters face-up
        if province.dynasty_cards:
            for new_card in province.dynasty_cards:
                if new_card.face_down:
                    new_card.turn_face_up()


@dataclass(repr=False, kw_only=True)
class KharmicAction(Ability):
    """Kharmic Repeatable Limited: Discard a Kharmic card from your hand to draw a card,
    or discard a Kharmic card from your Province to refill the Province face-up.
    """

    limited: bool = field(default=True, init=False)
    repeatable: bool = field(default=True, init=False)

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> Generator[Entity, None, None]:
        from .keywords import Kharmic

        # Kharmic cards in hand
        for card in active_player.hand[:]:
            if any(
                (isinstance(kw, type) and issubclass(kw, Kharmic)) or kw is Kharmic
                for kw in card.keywords
            ):
                yield card

        # Kharmic cards in provinces
        for province in active_player.provinces:
            for card in province.dynasty_cards:
                if card.face_up and any(
                    (isinstance(kw, type) and issubclass(kw, Kharmic)) or kw is Kharmic
                    for kw in card.keywords
                ):
                    yield card

    def pay_cost(self, game: Game, entity: Entity) -> bool:
        return True

    def get_effect(self, game: Game, card: Entity):
        from .errors import EndOfFateDeckError
        from .locations import ProvinceLocation

        if card.location is Hand:
            # Discard from hand, draw a card
            logging.info(
                "%s: Kharmic — discarding %s from hand to draw a card.",
                card.owner.name,
                card.title,
            )
            card.discard()
            try:
                card.owner.draw_fate_card()
            except EndOfFateDeckError:
                logging.info("%s: Fate deck is empty.", card.owner.name)
        elif card.location is ProvinceLocation:
            # Discard from province, refill face-up
            province = card.province
            logging.info(
                "%s: Kharmic — discarding %s from province to refill face-up.",
                card.owner.name,
                card.title,
            )
            province.dynasty_cards.remove(card)
            card.discard()
            province.fill()
            if province.dynasty_cards:
                for new_card in province.dynasty_cards:
                    if new_card.face_down:
                        new_card.turn_face_up()
