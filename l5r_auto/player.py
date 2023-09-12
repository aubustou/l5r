from __future__ import annotations

import logging
import random
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Sequence, Type

from l5r_auto.cards.holdings.common import HoldingEntity
from l5r_auto.clans import Clan

from .cards import DynastyCard, FateCard, SenseiEntity, StrongholdEntity
from .errors import EndOfDynastyDeckError, EndOfFateDeckError
from .locations import Hand, PlayArea, ProvinceLocation, StrongholdLocation

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
NAMES_BACKUP = NAMES.copy()
MINIMUM_HONOR = -20
STARTING_HAND_SIZE = 0
STARTING_NUMBER_OF_PROVINCES = 4
SUCCESSIVE_BATTLE_ACTIONS = 1


@dataclass(repr=False, kw_only=True)
class Player:
    name: str = field(default="")
    deck: Deck

    right_to: Player | None = None

    clan: Type[Clan] = field(init=False)
    stronghold: Stronghold = field(init=False)
    sensei: Sensei | None = field(init=False)

    hand: list[FateCard] = field(default_factory=list)
    provinces: list[ProvinceLocation] = field(default_factory=list)

    stronghold_entity: StrongholdEntity = field(init=False)
    sensei_entity: SenseiEntity | None = field(init=False)

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
            global NAMES
            if not NAMES:
                NAMES = NAMES_BACKUP.copy()

            chosen_name = random.choice(NAMES)
            NAMES.remove(chosen_name)
            self.name = f"{chosen_name}-{str(uuid.uuid4())[:4]}"
        self.stronghold = self.deck.stronghold
        self.sensei = self.deck.sensei
        self.clan = self.deck.clan

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
        self.entities = [
            x(game=game, current_legality=game.legality, owner=self)
            for x in self.deck.cards
        ]
        self.stronghold_entity = next(
            x for x in self.entities if isinstance(x, StrongholdEntity)
        )
        if self.sensei:
            self.sensei_entity = next(
                x for x in self.entities if isinstance(x, SenseiEntity)
            )
        else:
            self.sensei_entity = None
        self.fate_deck = [x for x in self.entities if isinstance(x, FateCard)]
        self.dynasty_deck = [x for x in self.entities if isinstance(x, DynastyCard)]

    def show_stronghold(self):
        logging.info("%s: Showing stronghold", self.name)
        self.stronghold_entity.turn_face_up()
        self.stronghold_entity.location = StrongholdLocation

    def show_sensei(self):
        if self.sensei:
            logging.info("%s: Showing sensei", self.name)
            self.sensei_entity.turn_face_up()
            self.sensei_entity.location = StrongholdLocation

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
        self.provinces.append(ProvinceLocation(player=self))

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
        card.move_to(Hand)

        return card

    def draw_dynasty_card(self) -> DynastyCard:
        logging.debug("%s: Drawing dynasty card", self.name)
        try:
            card = self.dynasty_deck.pop()
        except IndexError:
            raise EndOfDynastyDeckError
        card.move_to(ProvinceLocation)

        return card

    @property
    def holdings(self) -> list[HoldingEntity]:
        return [
            x
            for x in self.entities
            if isinstance(x, HoldingEntity) and x.location is PlayArea
        ]
