from __future__ import annotations

from dataclasses import dataclass, field
import uuid

from l5r_auto.card import Card
from l5r_auto.cards.strongholds.common import Stronghold


@dataclass(kw_only=True)
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(kw_only=True)
class Player:
    name: str
    honor: int
    right_to: Player

    hand: list[Card] = field(default_factory=list)
    provinces: list[Card] = field(default_factory=list)
    dynasty_deck: list[Card] = field(default_factory=list)
    fate_deck: list[Card] = field(default_factory=list)
    discard: list[Card] = field(default_factory=list)
    removed_from_game: list[Card] = field(default_factory=list)
    play_area: list[Card] = field(default_factory=list)
    stronghold: Stronghold | None = None

    entities: list[Entity] = field(default_factory=list)
