from __future__ import annotations

import logging
import uuid
from dataclasses import InitVar, field, fields
from typing import TYPE_CHECKING, Any, Type

from ..clans import Clan
from ..locations import FateDiscard, Location, ProvinceLocation
from ..utils import dataclass_ as dataclass
from ..utils import import_submodules

if TYPE_CHECKING:
    from ..abilities import Ability, Trait
    from ..keywords import Keyword
    from ..legality import Legality
    from ..locations import DynastyDiscard, RemovedFromGame
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


@dataclass
class Card:
    card_id: int = field(metadata={"is_written": True})
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    traits: list[Trait] = field(default_factory=list, metadata={"is_written": True})
    abilities: list[Ability] = field(
        default_factory=list, metadata={"is_written": True}
    )

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


@dataclass
class DynastyCard(Card):
    province: ProvinceLocation | None = field(default=None)


@dataclass
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


@dataclass
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    game: Game
    base_card: Type[Card]
    owner: Player

    current_legality: InitVar[Type[Legality]] | None = None

    title: str = field(metadata={"is_written": True})

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
        self.location = DynastyDiscard if isinstance(self, DynastyCard) else FateDiscard

    @log_state_change
    def remove_from_game(self):
        self.bowed = False
        self.location = RemovedFromGame

    @log_state_change
    def destroy(self):
        self.bowed = False
        self.location = DynastyDiscard if isinstance(self, DynastyCard) else FateDiscard

    @log_state_change
    def turn_face_down(self):
        self.face_down = True

    @log_state_change
    def turn_face_up(self):
        self.face_down = False


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
