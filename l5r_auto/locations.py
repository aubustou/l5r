from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cards import DynastyCard, FateCard
    from .player import Player


@dataclass(repr=False, kw_only=True)
class Location:
    player: Player

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__

    def __repr__(self) -> str:
        return self.__class__.__name__


@dataclass(repr=False, kw_only=True)
class Deck(Location):
    pass


@dataclass(repr=False, kw_only=True)
class Hand(Location):
    pass


@dataclass(repr=False, kw_only=True)
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


@dataclass(repr=False, kw_only=True)
class PlayArea(Location):
    pass


@dataclass(repr=False, kw_only=True)
class Discard(Location):
    pass


@dataclass(repr=False, kw_only=True)
class RemovedFromGame(Location):
    pass


@dataclass(repr=False, kw_only=True)
class StrongholdLocation(Location):
    pass


@dataclass(repr=False, kw_only=True)
class DynastyDeck(Deck):
    pass


@dataclass(repr=False, kw_only=True)
class FateDeck(Deck):
    pass


@dataclass(repr=False, kw_only=True)
class DynastyDiscard(Discard):
    pass


@dataclass(repr=False, kw_only=True)
class FateDiscard(Discard):
    pass


@dataclass(repr=False, kw_only=True)
class Battlefield(Location):
    terrain: FateCard = field(init=False)
