from __future__ import annotations

import uuid
from dataclasses import dataclass, field, fields
from typing import TYPE_CHECKING, Any, Type

from ..utils import import_submodules

if TYPE_CHECKING:
    from ..abilities import Ability, Trait
    from ..keywords import Keyword
    from ..legality import Legality
    from ..locations import DynastyDiscard, RemovedFromGame
    from ..play import Game


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


@dataclass(kw_only=True)
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
        return self.entity_type(*args, **kwds, **self.written())

    def to_string(self):
        return f"{self.title} ({self.id})"


@dataclass(kw_only=True)
class DynastyCard(Card):
    bowed: bool = False

    def destroy(self):
        self.location = DynastyDiscard

    def remove_from_game(self):
        self.location = RemovedFromGame


@dataclass(kw_only=True)
class FateCard(Card):
    gold_cost: int = field(metadata={"is_written": True})
    focus_value: int = field(metadata={"is_written": True})


@dataclass(kw_only=True)
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    game: Game
    title: str = field(metadata={"is_written": True})

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        return f"{self.title} ({self.id})"

    def target(self):
        pass

    def bow(self):
        pass

    def straighten(self):
        pass

    def dishonor(self):
        pass

    def rehonor(self):
        pass

    def discard(self):
        pass

    def remove_from_game(self):
        pass

    def destroy(self):
        pass


from .events.common import Event  # noqa
from .followers.common import Follower  # noqa
from .holdings.common import Holding  # noqa
from .items.common import Item  # noqa
from .personalities.common import Personality  # noqa
from .regions.common import Region  # noqa
from .rings.common import Ring  # noqa
from .senseis.common import Sensei  # noqa
from .spells.common import Spell  # noqa
from .strategies.common import Strategy  # noqa
from .strongholds.common import Stronghold  # noqa
