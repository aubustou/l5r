from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .card import Ability, Card
    from .cards.strongholds.common import Stronghold
    from .phases import Phase, Step


@dataclass(kw_only=True)
class Game:
    players: list[Player] = field(default_factory=list)

    current_player: Player | None = None
    current_phase: Phase | None = None
    current_step: Step | None = None


@dataclass(kw_only=True)
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    game: Game


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

    available_abilities: list[Ability] = field(default_factory=list)

    battle_actions: int = 1
