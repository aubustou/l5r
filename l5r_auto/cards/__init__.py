from __future__ import annotations

from typing import TYPE_CHECKING, Type

from ..utils import import_submodules
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

if TYPE_CHECKING:
    from ..card import Card


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
