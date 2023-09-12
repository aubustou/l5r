from __future__ import annotations

import logging
import uuid
from dataclasses import InitVar, dataclass, field, fields
from typing import TYPE_CHECKING, Any, Generator, Type

from ..clans import Clan
from ..locations import (
    DynastyDiscard,
    FateDiscard,
    Location,
    PlayArea,
    ProvinceLocation,
    RemovedFromGame,
    StrongholdLocation,
)
from ..utils import dataclass_, import_submodules

if TYPE_CHECKING:
    from ..abilities import Ability, Trait
    from ..keywords import Keyword
    from ..legality import Legality
    from ..play import Game
    from ..player import Player


CARDS: dict[Type[Card], dict[int, Card]] = {}
ALL_CARDS: dict[int, Card] = {}


def load_cards():
    import_submodules("l5r_auto.cards")
    global ALL_CARDS

    ALL_CARDS = {x.card_id: x for y in CARDS.values() for x in y.values()}


def get_card(card_id: int) -> Card | None:
    if not CARDS:
        load_cards()

    return ALL_CARDS.get(card_id)


def get_cards(card_type: Type[Card]) -> list[Card]:
    if not CARDS:
        load_cards()

    return list(CARDS[card_type].values())


@dataclass(repr=False, kw_only=True)
class BaseCard:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )


@dataclass(repr=False, kw_only=True)
class Card(BaseCard):
    card_id: int = field(metadata={"is_written": True})
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(metadata={"is_written": True})

    legality: list[Type[Legality]] = field(
        default_factory=list, metadata={"is_written": True}
    )

    entity_type: Type[Entity] = field(init=False)

    def __post_init__(self):
        CARDS.setdefault(self.__class__, {})[self.card_id] = self

    def written(self) -> dict[str, Any]:
        return {
            f.name: getattr(self, f.name)
            for f in fields(self)
            if f.metadata.get("is_written")
        }

    def __call__(self, *args: Any, **kwds: Any) -> Entity:
        # logging.debug(f"Creating {self.__class__.__name__} with {self.written()}")
        return self.entity_type(base_card=self, *args, **kwds, **self.written())

    def to_string(self):
        return f"{self.title} ({self.id})"


@dataclass(repr=False, kw_only=True)
class DynastyCard(Card):
    province: ProvinceLocation | None = field(default=None)


@dataclass(repr=False, kw_only=True)
class FateCard(Card):
    gold_cost: int = field(metadata={"is_written": True})
    focus_value: int = field(metadata={"is_written": True})


def log_state_change(method):
    def wrapper(self, *args, **kwargs):
        logging.debug(
            "%s: Changing state of %s with %s",
            self.owner.name,
            self.title,
            method.__name__,
        )
        method(self, *args, **kwargs)

    return wrapper


@dataclass(repr=False, kw_only=True)
class Entity(BaseCard):
    game: Game
    base_card: Type[Card]
    owner: Player

    current_legality: InitVar[Type[Legality]] | None = None

    # States
    bowed: bool = False
    face_down: bool = True  # By default, all cards are hidden

    location: Type[Location] = field(init=False)

    def __post_init__(self, current_legality: Type[Legality] | None = None):
        if current_legality and hasattr(self, "clan"):
            self.clan = [x for x in self.clan if x in current_legality.legal_clans]

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        return f"{self.title} ({self.id})"

    @property
    def entity_type(self) -> Type[Entity]:
        return self.base_card.entity_type

    @property
    def face_up(self) -> bool:
        return not self.face_down

    def move_to(self, to_location: Type[Location]):
        from_location = self.location
        self.location = to_location
        from_location_name = from_location.get_name()
        to_location_name = to_location.get_name()
        logging.debug(
            "%s: Moving %s from %s to %s",
            self.owner.name,
            self.title,
            from_location_name,
            to_location_name,
        )

        match from_location_name:
            case "PlayArea":
                self.owner.play_area.remove(self)
            case "DynastyDiscard":
                self.owner.dynasty_discard.remove(self)
            case "FateDiscard":
                self.owner.fate_discard.remove(self)
            case "RemovedFromGame":
                self.owner.removed_from_game.remove(self)
            case "DynastyDeck":
                self.owner.dynasty_deck.remove(self)
            case "FateDeck":
                self.owner.fate_deck.remove(self)
            case "Hand":
                self.owner.hand.remove(self)
            case "ProvinceLocation" | "StrongholdLocation" | "Deck":
                pass
            case _:
                logging.warning("Unknown location %s", from_location)
        match to_location_name:
            case "PlayArea":
                self.owner.play_area.append(self)
            case "DynastyDiscard":
                self.owner.dynasty_discard.append(self)
            case "FateDiscard":
                self.owner.fate_discard.append(self)
            case "RemovedFromGame":
                self.owner.removed_from_game.append(self)
            case "DynastyDeck":
                self.owner.dynasty_deck.append(self)
            case "FateDeck":
                self.owner.fate_deck.append(self)
            case "Hand":
                self.owner.hand.append(self)
            case "ProvinceLocation" | "StrongholdLocation" | "Deck":
                pass
            case _:
                logging.warning("Unknown location %s", to_location)

    @log_state_change
    def target(self):
        pass

    @log_state_change
    def bow(self):
        self.bowed = True

    @log_state_change
    def straighten(self):
        self.bowed = False

    @log_state_change
    def discard(self):
        self.bowed = False
        self.move_to(DynastyDiscard if isinstance(self, DynastyCard) else FateDiscard)

    @log_state_change
    def remove_from_game(self):
        self.bowed = False
        self.move_to(RemovedFromGame)

    @log_state_change
    def destroy(self):
        self.bowed = False
        self.move_to(DynastyDiscard if isinstance(self, DynastyCard) else FateDiscard)

    @log_state_change
    def turn_face_down(self):
        self.face_down = True

    @log_state_change
    def turn_face_up(self):
        self.face_down = False

    def on_pay(
        self, game: Game, player: Player, entity: Entity
    ) -> Generator[int, None, None]:
        yield from (x.on_pay(game, player, entity) for x in self.abilities)

    gold_amount: int = 0

    @property
    def can_produce(self) -> bool:
        return (
            self.location in {PlayArea, StrongholdLocation}
            and getattr(self, "gold_production", None) is not None
            and self.face_up
            and not self.bowed
        )


from .events.common import Event, EventEntity  # noqa
from .followers.common import Follower, FollowerEntity  # noqa
from .holdings.common import Holding, HoldingEntity  # noqa
from .items.common import Item, ItemEntity  # noqa
from .personalities.common import Personality, PersonalityEntity  # noqa
from .regions.common import Region, RegionEntity  # noqa
from .rings.common import Ring, RingEntity  # noqa
from .senseis.common import Sensei, SenseiEntity  # noqa
from .spells.common import Spell, SpellEntity  # noqa
from .strategies.common import Strategy, StrategyEntity  # noqa
from .strongholds.common import Stronghold, StrongholdEntity  # noqa
