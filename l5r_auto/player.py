from __future__ import annotations

import logging
import random
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Sequence

from .cards import DynastyCard, FateCard
from .errors import EndOfDynastyDeckError, EndOfFateDeckError
from .locations import ProvinceLocation

if TYPE_CHECKING:
    from .abilities import Ability
    from .cards import Entity, Sensei, Stronghold
    from .deck import Deck
    from .models import PlayerReport
    from .play import Game


NAMES = [
    "Simon",
    "Manu",
    "Pierre",
    "François",
    "Vincent",
    "Picasso",
    "c'est pas dans l'environnement",
    "le rat",
    "immonde bâtard",
    "Michel Muller",
]
MINIMUM_HONOR = -20
STARTING_HAND_SIZE = 0
STARTING_NUMBER_OF_PROVINCES = 4
SUCCESSIVE_BATTLE_ACTIONS = 1


@dataclass(kw_only=True)
class Player:
    name: str = field(default="")
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
        if not self.name:
            self.name = f"{random.choice(NAMES)}-{str(uuid.uuid4())[:4]}"
        self.stronghold = self.deck.stronghold
        self.sensei = self.deck.sensei

    def report(self):
        return PlayerReport(
            name=self.name,
            deck=str(self.deck.id),
            stronghold=self.stronghold.title,
            sensei=self.sensei.title if self.sensei else None,
            hand=[x.title for x in self.hand],
            provinces=[x.report() for x in self.provinces],
            dynasty_deck=[x.title for x in self.dynasty_deck],
            fate_deck=[x.title for x in self.fate_deck],
            dynasty_discard=[x.title for x in self.dynasty_discard],
            fate_discard=[x.title for x in self.fate_discard],
            removed_from_game=[x.title for x in self.removed_from_game],
            play_area=[x.title for x in self.play_area],
        )

    def create_entities(self, game: Game):
        self.entities = [x(game=game) for x in self.deck.cards]
        self.fate_deck = [x for x in self.entities if isinstance(x, FateCard)]
        self.dynasty_deck = [x for x in self.entities if isinstance(x, DynastyCard)]

    def set_starting_honor(self):
        self.honor = self.deck.stronghold.starting_family_honor + (
            self.sensei.starting_family_honor if self.sensei else 0
        )
        logging.debug("%s: Set starting honor to %d", self.name, self.honor)

    def shuffle_decks(self):
        self.shuffle_fate_deck()
        self.shuffle_dynasty_deck()

    def shuffle_fate_deck(self):
        random.shuffle(self.fate_deck)
        logging.debug("%s: Shuffled fate deck", self.name)
        for card in self.fate_deck:
            logging.debug("\t%s", card.to_string())

    def shuffle_dynasty_deck(self):
        random.shuffle(self.dynasty_deck)
        logging.debug("%s: Shuffled dynasty deck", self.name)
        for card in self.dynasty_deck:
            logging.debug("\t%s", card.to_string())

    def create_province(self):
        logging.debug("%s: Creating province", self.name)
        self.provinces.append(
            ProvinceLocation(dynasty_cards=[self.draw_dynasty_card()])
        )

    def create_provinces(self):
        logging.debug("%s: Creating provinces", self.name)
        for _ in range(self.number_of_provinces):
            self.create_province()

    def draw_hand(self):
        logging.debug("%s: Drawing hand", self.name)
        self.hand = [self.draw_fate_card() for _ in range(self.hand_size)]

    def draw_fate_card(self) -> FateCard:
        logging.debug("%s: Drawing fate card", self.name)
        try:
            card = self.fate_deck.pop()
        except IndexError:
            raise EndOfFateDeckError
        return card

    def draw_dynasty_card(self) -> DynastyCard:
        logging.debug("%s: Drawing dynasty card", self.name)
        try:
            card = self.dynasty_deck.pop()
        except IndexError:
            raise EndOfDynastyDeckError

        return card
