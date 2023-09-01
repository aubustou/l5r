from __future__ import annotations

import itertools
import logging
import random
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Sequence

from l5r_auto.errors import EndOfDynastyDeckError, EndOfFateDeckError
from l5r_auto.phases import StartOfGame, Turn, TurnSequences

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
    current_turn: Turn = field(init=False)
    current_phase: Phase = None
    current_step: Step | None = None

    starting_player: Player | None = field(init=False)

    phases: list[Phase] = field(default_factory=list)

    steps = [
        StartOfGame,
        TurnSequences,
    ]

    def __post_init__(self):
        if len(self.players) > 1:
            # Placing players
            for left, right in itertools.cycle(itertools.pairwise(self.players)):
                if left.right_to is None:
                    left.right_to = right
                else:
                    break

        for player in self.players:
            # Generate card entities before starting game
            player.create_entities(game=self)

    def start(self):
        logging.info("Starting game: %s", self.id)
        for step in self.steps:
            self.current_step = step(game=self)
            self.current_step.start()

    def take_turn(self, number: int, active_player: Player):
        self.current_turn = Turn(number=number, active_player=active_player)

    def report(self):
        pass


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

    def create_entities(self, game: Game):
        self.entities = [x(game=game) for x in self.deck.cards]
        self.fate_deck = [x for x in self.entities if isinstance(x, FateCard)]
        self.dynasty_deck = [x for x in self.entities if isinstance(x, DynastyCard)]

    def set_starting_honor(self):
        self.honor = self.deck.stronghold.starting_family_honor + (
            self.sensei.starting_family_honor if self.sensei else 0
        )
        logging.debug("Set starting honor for %s to %d", self.name, self.honor)

    def shuffle_decks(self):
        random.shuffle(self.fate_deck)
        logging.debug(f"Shuffled fate deck:")
        for card in self.fate_deck:
            logging.debug(f"\t{card.to_string()}")

        random.shuffle(self.dynasty_deck)
        logging.debug(f"Shuffled dynasty deck:")
        for card in self.dynasty_deck:
            logging.debug(f"\t{card.to_string()}")

    def create_provinces(self):
        logging.debug("Creating provinces for %s", self.name)
        self.provinces = [
            ProvinceLocation(dynasty_cards=[self.draw_dynasty_card()])
            for _ in range(self.number_of_provinces)
        ]

    def draw_hand(self):
        logging.debug("Drawing hand for %s", self.name)
        self.hand = [self.draw_fate_card() for _ in range(self.hand_size)]

    def draw_fate_card(self) -> FateCard:
        logging.debug("Drawing fate card for %s", self.name)
        try:
            card = self.fate_deck.pop()
        except IndexError:
            raise EndOfFateDeckError
        return card

    def draw_dynasty_card(self) -> DynastyCard:
        logging.debug("Drawing dynasty card for %s", self.name)
        try:
            card = self.dynasty_deck.pop()
        except IndexError:
            raise EndOfDynastyDeckError

        return card
