from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .card import FateCard
    from .player import DynastyCardEntity


@dataclass(kw_only=True)
class Location:
    pass


@dataclass(kw_only=True)
class Deck(Location):
    pass


@dataclass(kw_only=True)
class Hand(Location):
    pass


@dataclass(kw_only=True)
class ProvinceLocation(Location):
    dynasty_cards: list[DynastyCardEntity] = field(default_factory=list)
    attachments: list[DynastyCardEntity] = field(default_factory=list)


@dataclass(kw_only=True)
class PlayArea(Location):
    pass


@dataclass(kw_only=True)
class Discard(Location):
    pass


@dataclass(kw_only=True)
class RemovedFromGame(Location):
    pass


@dataclass(kw_only=True)
class Stronghold(Location):
    pass


@dataclass(kw_only=True)
class DynastyDeck(Deck):
    pass


@dataclass(kw_only=True)
class FateDeck(Deck):
    pass


@dataclass(kw_only=True)
class DynastyDiscard(Discard):
    pass


@dataclass(kw_only=True)
class FateDiscard(Discard):
    pass


@dataclass(kw_only=True)
class Battlefield(Location):
    terrain: FateCard = field(init=False)
