from __future__ import annotations

import json
import logging
import uuid
from dataclasses import field, fields
from functools import cached_property
from operator import attrgetter
from typing import TYPE_CHECKING, Sequence, Type, TypedDict

from l5r_auto.cards import get_card
from l5r_auto.utils import dataclass_ as dataclass

from .cards import Card
from .clans import Clan, clans
from .legality import Legality, legalities

if TYPE_CHECKING:
    from .cards import (
        Event,
        Follower,
        Holding,
        Item,
        Personality,
        Region,
        Ring,
        Sensei,
        Spell,
        Strategy,
        Stronghold,
    )


class DeckEncoder(json.JSONEncoder):
    def default(self, o):
        logging.debug("DeckEncoder: %s", o)
        if isinstance(o, type) and issubclass(o, (Clan, Legality)):
            return o.name
        if isinstance(o, Card):
            return o.card_id
        else:
            return json.JSONEncoder.default(self, o)


class DeckDict(TypedDict):
    clan: Type[Clan]
    legality: Type[Legality]
    stronghold: Card
    personalities: list[Personality]
    holdings: list[Holding]
    events: list[Event]


class DeckJSON(TypedDict):
    clan: str
    legality: str
    stronghold: int
    personalities: list[int]
    holdings: list[int]
    events: list[int]


@dataclass
class Deck:
    clan: Type[Clan]
    legality: Type[Legality]
    version: int = 1
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    former_version_id: uuid.UUID | None = None

    stronghold: Stronghold = field(init=False, metadata={"are_cards": True})
    sensei: Sensei | None = field(
        default=None, init=False, metadata={"are_cards": True}
    )
    # Dynasty
    events: list[Event] = field(default_factory=list, metadata={"are_cards": True})
    holdings: list[Holding] = field(default_factory=list, metadata={"are_cards": True})
    personalities: list[Personality] = field(
        default_factory=list, metadata={"are_cards": True}
    )
    regions: list[Region] = field(default_factory=list, metadata={"are_cards": True})
    # Fate
    followers: list[Follower] = field(
        default_factory=list, metadata={"are_cards": True}
    )
    items: list[Item] = field(default_factory=list, metadata={"are_cards": True})
    rings: list[Ring] = field(default_factory=list, metadata={"are_cards": True})
    spells: list[Spell] = field(default_factory=list, metadata={"are_cards": True})
    strategies: list[Strategy] = field(
        default_factory=list, metadata={"are_cards": True}
    )

    @cached_property
    def cards(self) -> Sequence[Card]:
        cards: Sequence[Card] = []
        for field in fields(self):
            if field.metadata.get("are_cards"):
                if isinstance(value := getattr(self, field.name), list):
                    cards.extend(value)
                elif value is not None:
                    cards.append(value)

        return cards

    def to_dict(self) -> DeckDict:
        return {
            "clan": self.clan,
            "legality": self.legality,
            "stronghold": self.stronghold,
            "personalities": self.personalities,
            "holdings": self.holdings,
            "events": self.events,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4, cls=DeckEncoder)

    @classmethod
    def from_json(cls, json_: str) -> Deck:
        deck_list: DeckJSON = json.loads(json_)
        if not (clan := next((x for x in clans if x.name == deck_list["clan"]), None)):
            raise ValueError(f"Unknown clan: {deck_list['clan']}")
        if not (
            legality := next(
                (
                    x
                    for x in legalities
                    if x.name.lower() == deck_list["legality"].lower()
                ),
                None,
            )
        ):
            raise ValueError(f"Unknown legality: {deck_list['legality']}")

        deck = cls(clan=clan, legality=legality)
        if not (stronghold_card := get_card(deck_list["stronghold"])):
            raise ValueError(f"Unknown stronghold: {deck_list['stronghold']}")
        deck.stronghold = stronghold_card

        for personality_id in deck_list["personalities"]:
            if not (personality_card := get_card(personality_id)):
                raise ValueError(f"Unknown personality: {personality_id}")
            deck.personalities.append(personality_card)

        for holding_id in deck_list["holdings"]:
            if not (holding_card := get_card(holding_id)):
                raise ValueError(f"Unknown holding: {holding_id}")
            deck.holdings.append(holding_card)

        for event_id in deck_list["events"]:
            if not (event_card := get_card(event_id)):
                raise ValueError(f"Unknown event: {event_id}")
            deck.events.append(event_card)

        return deck

    def __str__(self) -> str:
        return f"Deck with {self.stronghold.title}"

    def add(self, card: Card):
        match card.__class__.__name__:
            case "Personality":
                self.personalities.append(card)
            case "Holding":
                self.holdings.append(card)
            case "Event":
                self.events.append(card)
            case _:
                raise ValueError(f"Unknown card type: {card.__class__.__name__}")

    def show(self):
        logging.info("Deck %s %s", self.clan.name, self.legality.name)
        logging.debug("Deck id: %s", self.id)
        logging.debug("Deck version: %s", self.version)

        logging.info("Stronghold: %s", self.stronghold.title)

        logging.info("Personalities: %s", len(self.personalities))
        for personality in sorted(self.personalities, key=attrgetter("title")):
            logging.info("\t%s", personality.title)
        logging.info(
            "Average personality cost: %1.2f", self.average_personalities_cost()
        )

        logging.info("Holdings: %s", len(self.holdings))
        for holding in sorted(self.holdings, key=attrgetter("title")):
            logging.info("\t%s", holding.title)
        logging.info("Average holding cost: %1.2f", self.average_holdings_cost())

        logging.info("Events: %s", len(self.events))
        for event in sorted(self.events, key=attrgetter("title")):
            logging.info("\t%s", event.title)

    def average_personalities_cost(self) -> float:
        return sum(x.gold_cost for x in self.personalities) / len(self.personalities)

    def average_holdings_cost(self) -> float:
        return sum(x.gold_cost for x in self.holdings) / len(self.holdings)
