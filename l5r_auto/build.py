from __future__ import annotations

import logging
import random
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, Sequence, Type

from l5r_auto.cards.events.common import get_cards as get_events
from l5r_auto.cards.followers.common import get_cards as get_followers
from l5r_auto.cards.holdings.common import get_cards as get_holdings
from l5r_auto.cards.items.common import get_cards as get_items
from l5r_auto.cards.spells.common import get_cards as get_spells
from l5r_auto.cards.strategies.common import get_cards as get_strategies

from .cards.personalities.common import get_cards as get_personalities
from .cards.strongholds.common import get_cards as get_strongholds
from .clans import Clan, Unaligned, clans
from .deck import Deck
from .legality import Legality, legalities

if TYPE_CHECKING:
    from .cards import Card


DECK_FOLDER = Path(__file__).parent / "decks"

MAX_COPIES_PER_CARD = 3
MIN_GOLD_PRODUCERS = 6


def _is_unique(card: Card) -> bool:
    from l5r_auto.keywords import Unique

    return any(
        (isinstance(kw, type) and issubclass(kw, Unique)) or kw is Unique
        for kw in card.keywords
    )


def _get_experienced_base_title(card: Card) -> str | None:
    """Return the base title for an Experienced card, or None if not Experienced."""
    from l5r_auto.keywords import Keyword

    for kw in card.keywords:
        if isinstance(kw, type) and hasattr(kw, "level"):
            return card.title
    return None


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
        case "followers":
            cards = get_followers(legality)
        case "items":
            cards = get_items(legality)
        case "strategies":
            cards = get_strategies(legality)
        case "spells":
            cards = get_spells(legality)
        case _:
            raise ValueError(f"Unknown card type: {type_}")

    # Filter clan-aligned cards: only own clan + unaligned
    if type_ == "personalities":
        cards = [
            c for c in cards
            if not hasattr(c, "clan") or not c.clan
            or clan in c.clan
            or Unaligned in c.clan
        ]

    if not cards:
        logging.info("No %s cards found for %s %s.", type_, legality.name, clan.name)
        return

    copy_counts: Counter = Counter(c.card_id for c in deck.personalities + deck.holdings + deck.events + deck.followers + deck.items + deck.strategies + deck.spells)

    for _ in range(number):
        eligible = [
            c for c in cards
            if copy_counts[c.card_id] < (_is_unique(c) and 1 or MAX_COPIES_PER_CARD)
        ]
        if not eligible:
            eligible = cards
        card = random.choice(eligible)
        deck.add(card)
        copy_counts[card.card_id] += 1


def _ensure_gold_distribution(deck: Deck, legality: Type[Legality]):
    """Ensure the deck has at least MIN_GOLD_PRODUCERS gold-producing holdings."""
    gold_producers = [h for h in deck.holdings if getattr(h, "gold_production", 0)]
    shortfall = MIN_GOLD_PRODUCERS - len(gold_producers)
    if shortfall <= 0:
        return

    logging.info(
        "Deck has only %d gold producer(s); adding %d more.",
        len(gold_producers),
        shortfall,
    )
    all_holdings = get_holdings(legality)
    producing_holdings = [h for h in all_holdings if getattr(h, "gold_production", 0)]
    if not producing_holdings:
        return

    for _ in range(shortfall):
        card = random.choice(producing_holdings)
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

    strongholds = get_strongholds(legality_, clan_)
    if not strongholds:
        # Onyx Edition reuses Emperor Edition strongholds
        from .legality import EmperorEdition
        strongholds = get_strongholds(EmperorEdition, clan_)
    if not strongholds:
        raise ValueError("No strongholds found")
    logging.info("Found %s strongholds", len(strongholds))
    stronghold = random.choice(strongholds)

    deck.stronghold = stronghold

    logging.info("Fetching dynasty cards...")
    logging.info("Fetching personalities...")
    fetch_cards(deck, legality_, clan_, "personalities", 12)

    logging.info("Fetching holdings...")
    fetch_cards(deck, legality_, clan_, "holdings", 11)
    _ensure_gold_distribution(deck, legality_)

    logging.info("Fetching events...")
    fetch_cards(deck, legality_, clan_, "events", 2)

    logging.info("Fetching fate cards...")
    logging.info("Fetching strategies...")
    fetch_cards(deck, legality_, clan_, "strategies", 10)

    logging.info("Fetching followers...")
    fetch_cards(deck, legality_, clan_, "followers", 5)

    logging.info("Fetching items...")
    fetch_cards(deck, legality_, clan_, "items", 5)

    return deck


def main():
    logging.basicConfig(level=logging.DEBUG)

    target_legalities = ["emperor", "onyx", "20f"]

    for legality_short in target_legalities:
        legality_ = next(
            (x for x in legalities if legality_short.lower() in {x.name.lower(), x.acronym.lower(), x.short.lower()}),
            None,
        )
        if not legality_:
            logging.warning("Unknown legality: %s", legality_short)
            continue

        for clan in legality_.legal_clans:
            try:
                deck = build_deck(legality_.short, clan.name)
            except ValueError as e:
                logging.info("Skipping %s %s: %s", legality_.name, clan.name, e)
                continue

            deck.show()

            folder = DECK_FOLDER / deck.legality.name.lower() / deck.clan.name.lower()
            folder.mkdir(parents=True, exist_ok=True)

            (folder / f"{deck.id}.json").write_text(deck.to_json())


if __name__ == "__main__":
    main()
