from __future__ import annotations

import logging
import random
from dataclasses import dataclass, field
from operator import attrgetter
from typing import TYPE_CHECKING, Type

from l5r_auto.cards.events.common import Event, get_events
from l5r_auto.cards.holdings.common import Holding, get_holdings

from .cards.personalities.common import Personality, get_personalities
from .cards.strongholds.common import get_strongholds
from .clans import Clan, clans
from .legality import Legality, legalities

if TYPE_CHECKING:
    from l5r_auto.card import Card

    from .cards.strongholds.common import Stronghold


@dataclass(kw_only=True)
class Deck:
    clan: Type[Clan]
    legality: Type[Legality]

    stronghold: Type[Stronghold] = field(init=False)
    personalities: list[Type[Personality]] = field(default_factory=list)
    holdings: list[Type[Holding]] = field(default_factory=list)
    events: list[Type[Event]] = field(default_factory=list)

    def to_list(self) -> list[Type[Card]]:
        if not self.stronghold:
            raise ValueError("Deck must have a stronghold")
        return [self.stronghold]

    def __str__(self) -> str:
        return f"Deck with {self.stronghold.title}"

    def add(self, card: Type[Card]):
        match card.__class__.__name__:
            case "Personality":
                self.personalities.append(card)
            case "Holding":
                self.holdings.append(card)
            case "Event":
                self.events.append(card)
            case _:
                raise ValueError(f"Unknown card type: {card.__name__}")

    def show(self):
        logging.info("Deck %s %s", self.clan.name, self.legality.name)
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


def fetch_cards(
    deck: Deck, legality: Type[Legality], clan: Type[Clan], type_: str, number: int
):
    cards: list[Type[Card]]
    match type_:
        case "personalities":
            cards = get_personalities(legality, clan)
        case "holdings":
            cards = get_holdings(legality)
        case "events":
            cards = get_events(legality)
        case _:
            raise ValueError(f"Unknown card type: {type_}")

    for _ in range(number):
        card = random.choice(cards)
        deck.add(card)


def build_deck(legality: str, clan: str) -> Deck:
    if not (
        legality_ := next(
            (
                x
                for x in legalities
                if legality.lower()
                in {x.name.lower(), x.acronym.lower(), x.short.lower()}
            ),
            None,
        )
    ):
        raise ValueError(f"Unknown legality: {legality}")

    if not (
        clan_ := next(
            (
                x
                for x in clans
                if clan.lower() in {x.name.lower(), *[y.lower() for y in x.alternative]}
            ),
            None,
        )
    ):
        raise ValueError(f"Unknown clan: {clan}")

    logging.info("Building %s %s deck...", legality_.name, clan_.name)

    deck = Deck(clan=clan_, legality=legality_)
    logging.info("Fetching stronghold...")

    if strongholds := get_strongholds(legality_, clan_):
        logging.info("Found %s strongholds", len(strongholds))
        stronghold = random.choice(get_strongholds(legality_, clan_))
    else:
        raise ValueError("No strongholds found")

    deck.stronghold = stronghold

    logging.info("Fetching dynasty cards...")
    logging.info("Fetching personalities...")
    fetch_cards(deck, legality_, clan_, "personalities", 12)

    logging.info("Fetching holdings...")
    fetch_cards(deck, legality_, clan_, "holdings", 11)

    logging.info("Fetching events...")
    fetch_cards(deck, legality_, clan_, "events", 2)

    return deck


def main():
    logging.basicConfig(level=logging.DEBUG)

    deck = build_deck("20f", "dragon")
    deck.show()


if __name__ == "__main__":
    main()
