from __future__ import annotations

import logging
import random
from pathlib import Path
from typing import TYPE_CHECKING, Sequence, Type

from l5r_auto.cards.events.common import get_cards as get_events
from l5r_auto.cards.holdings.common import get_cards as get_holdings

from .card import Card
from .cards.personalities.common import get_cards as get_personalities
from .cards.strongholds.common import get_cards as get_strongholds
from .clans import Clan, clans
from .deck import Deck
from .legality import Legality, legalities

if TYPE_CHECKING:
    pass


DECK_FOLDER = Path(__file__).parent / "decks"


def fetch_cards(
    deck: Deck, legality: Type[Legality], clan: Type[Clan], type_: str, number: int
):
    cards: Sequence[Card]
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
        # TODO: check if card is unique
        # TODO: check if card is restricted
        # TODO: check if less than 3 copies of card
        # TODO: manage card gold cost distribution (gaussian distribution)
        # TODO: manage unaligned cards
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
        stronghold = random.choice(strongholds)
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

    for _ in range(20):
        for clan in [
            "crab",
            "crane",
            "dragon",
            "lion",
            "phoenix",
            "scorpion",
            "spider",
            "unicorn",
        ]:
            deck = build_deck("20f", clan)
            deck.show()

            folder = DECK_FOLDER / deck.legality.name.lower() / deck.clan.name.lower()
            folder.mkdir(parents=True, exist_ok=True)

            (folder / f"{deck.id}.json").write_text(deck.to_json())


if __name__ == "__main__":
    main()
