from __future__ import annotations

import logging
from dataclasses import field
from typing import TYPE_CHECKING

from .utils import dataclass_ as dataclass

if TYPE_CHECKING:
    from .cards import DynastyCard, FateCard
    from .player import Player


@dataclass
class Location:
    player: Player

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__

    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclass
class Deck(Location):
    pass


@dataclass
class Hand(Location):
    pass


@dataclass
class ProvinceLocation(Location):
    dynasty_cards: list[DynastyCard] = field(default_factory=list)
    attachments: list[DynastyCard] = field(default_factory=list)

    def __post_init__(self, *args, **kwargs):
        self.fill()

    def fill(self):
        logging.info("%s: Filling province: %s", self.player.name, self)
        card = self.player.draw_dynasty_card()
        card.province = self
        self.dynasty_cards.append(card)


@dataclass
class PlayArea(Location):
    pass


@dataclass
class Discard(Location):
    pass


@dataclass
class RemovedFromGame(Location):
    pass


@dataclass
class StrongholdLocation(Location):
    pass


@dataclass
class DynastyDeck(Deck):
    pass


@dataclass
class FateDeck(Deck):
    pass


@dataclass
class DynastyDiscard(Discard):
    pass


@dataclass
class FateDiscard(Discard):
    pass


@dataclass
class Battlefield(Location):
    terrain: FateCard = field(init=False)
