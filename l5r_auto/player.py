from __future__ import annotations

import logging
import random
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Sequence

from l5r_auto.errors import EndOfDynastyDeckError, EndOfFateDeckError

from .card import DynastyCard, FateCard
from .locations import ProvinceLocation

if TYPE_CHECKING:
    from .card import Ability
    from .cards import Sensei, Stronghold
    from .cards.strongholds.common import Stronghold
    from .deck import Deck
    from .phases import Phase, Step


@dataclass(kw_only=True)
class Game:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    players: list[Player]

    current_player: Player | None = None
    current_phase: Phase | None = None
    current_step: Step | None = None


@dataclass(kw_only=True)
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    game: Game

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        return f"{self.title} ({self.id})"


MINIMUM_HONOR = -20
STARTING_HAND_SIZE = 0
STARTING_NUMBER_OF_PROVINCES = 4
SUCCESSIVE_BATTLE_ACTIONS = 1


@dataclass(kw_only=True)
class Player:
    name: str
    deck: Deck

    right_to: Player | None = None

    stronghold: Stronghold | None = None
    sensei: Sensei | None = None

    hand: list[FateCard] = field(default_factory=list)
    provinces: list[ProvinceLocation] = field(default_factory=list)

    dynasty_deck: list[DynastyCard] = field(default_factory=list)
    fate_deck: list[FateCard] = field(default_factory=list)
    dynasty_discard: list[DynastyCard] = field(default_factory=list)
    fate_discard: list[FateCard] = field(default_factory=list)
    removed_from_game: list[Entity] = field(default_factory=list)
    play_area: list[Entity] = field(default_factory=list)

    entities: Sequence[Entity] = field(default_factory=list)

    available_abilities: list[Ability] = field(default_factory=list)

    honor: int = MINIMUM_HONOR
    number_of_provinces: int = STARTING_NUMBER_OF_PROVINCES
    hand_size: int = STARTING_HAND_SIZE
    successive_battle_actions: int = SUCCESSIVE_BATTLE_ACTIONS

    def __post_init__(self):
        self.stronghold = self.deck.stronghold
        self.sensei = self.deck.sensei
        self.honor = self.deck.stronghold.starting_family_honor + (
            self.sensei.starting_family_honor if self.sensei else 0
        )

    def create_entities(self, game: Game):
        self.entities = [x(game=game) for x in self.deck.cards]

    def prepare(self, game: Game):
        self.create_entities(game=game)

        self.fate_deck = [x for x in self.entities if isinstance(x, FateCard)]
        random.shuffle(self.fate_deck)
        logging.debug(f"Shuffled fate deck:")
        for card in self.fate_deck:
            logging.debug(f"\t{card.to_string()}")

        self.dynasty_deck = [x for x in self.entities if isinstance(x, DynastyCard)]
        random.shuffle(self.dynasty_deck)
        logging.debug(f"Shuffled dynasty deck:")
        for card in self.dynasty_deck:
            logging.debug(f"\t{card.to_string()}")

        self.provinces = [
            ProvinceLocation(dynasty_cards=[self.draw_dynasty_card()])
            for _ in range(self.number_of_provinces)
        ]
        self.hand = [self.draw_fate_card() for _ in range(self.hand_size)]

    def draw_fate_card(self) -> FateCard:
        try:
            card = self.fate_deck.pop()
        except IndexError:
            raise EndOfFateDeckError
        return card

    def draw_dynasty_card(self) -> DynastyCard:
        try:
            card = self.dynasty_deck.pop()
        except IndexError:
            raise EndOfDynastyDeckError

        return card
