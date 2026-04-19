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
from .legality import GameRules, Legality, legalities

if TYPE_CHECKING:
    from .cards import Card


DECK_FOLDER = Path(__file__).parent / "decks"


def _is_unique(card: Card) -> bool:
    from l5r_auto.keywords import Unique

    return any(
        (isinstance(kw, type) and issubclass(kw, Unique)) or kw is Unique
        for kw in card.keywords
    )


def _get_experienced_base_title(card: Card) -> str | None:
    """Return the base title for an Experienced card, or None if not Experienced."""

    for kw in card.keywords:
        if isinstance(kw, type) and hasattr(kw, "level"):
            return card.title
    return None


def fetch_cards(
    deck: Deck,
    legality: Type[Legality],
    clan: Type[Clan],
    type_: str,
    number: int,
    rules: GameRules,
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
            c
            for c in cards
            if not hasattr(c, "clan")
            or not c.clan
            or clan in c.clan
            or Unaligned in c.clan
        ]

    if not cards:
        logging.info("No %s cards found for %s %s.", type_, legality.name, clan.name)
        return

    copy_counts: Counter = Counter(
        c.card_id
        for c in deck.personalities
        + deck.holdings
        + deck.events
        + deck.followers
        + deck.items
        + deck.strategies
        + deck.spells
    )

    for _ in range(number):
        eligible = [
            c
            for c in cards
            if copy_counts[c.card_id]
            < (1 if _is_unique(c) else rules.max_copies_per_card)
        ]
        if not eligible:
            eligible = cards
        card = random.choice(eligible)
        deck.add(card)
        copy_counts[card.card_id] += 1


def _ensure_gold_distribution(deck: Deck, legality: Type[Legality], rules: GameRules):
    """Ensure the deck has at least rules.min_gold_producers gold-producing holdings."""
    gold_producers = [h for h in deck.holdings if getattr(h, "gold_production", 0)]
    shortfall = rules.min_gold_producers - len(gold_producers)
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

    rules = legality_.rules
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
    fetch_cards(
        deck, legality_, clan_, "personalities", rules.deck_personalities, rules
    )

    logging.info("Fetching holdings...")
    fetch_cards(deck, legality_, clan_, "holdings", rules.deck_holdings, rules)
    _ensure_gold_distribution(deck, legality_, rules)

    logging.info("Fetching events...")
    fetch_cards(deck, legality_, clan_, "events", rules.deck_events, rules)

    logging.info("Fetching fate cards...")
    logging.info("Fetching strategies...")
    fetch_cards(deck, legality_, clan_, "strategies", rules.deck_strategies, rules)

    logging.info("Fetching followers...")
    fetch_cards(deck, legality_, clan_, "followers", rules.deck_followers, rules)

    logging.info("Fetching items...")
    fetch_cards(deck, legality_, clan_, "items", rules.deck_items, rules)

    return deck


def generate_two_decks(legality_short: str | None = None) -> tuple[Deck, Deck]:
    """Build two decks from different clans for the same legality."""
    target_legalities = ["emperor", "onyx", "20f"]

    if legality_short is None:
        legality_short = random.choice(target_legalities)

    legality_ = next(
        (
            x
            for x in legalities
            if legality_short.lower()
            in {x.name.lower(), x.acronym.lower(), x.short.lower()}
        ),
        None,
    )
    if not legality_:
        raise ValueError(f"Unknown legality: {legality_short}")

    available_clans = list(legality_.legal_clans)
    if len(available_clans) < 2:
        raise ValueError(
            f"Not enough clans in {legality_.name} to build two decks"
        )

    deck1 = deck2 = None
    random.shuffle(available_clans)
    for clan in available_clans:
        try:
            d = build_deck(legality_.short, clan.name)
        except ValueError:
            continue
        if deck1 is None:
            deck1 = d
        else:
            deck2 = d
            break

    if deck1 is None or deck2 is None:
        raise ValueError(
            f"Could not build two decks for legality {legality_.name}"
        )

    return deck1, deck2


def _save_deck(deck: Deck) -> Path:
    folder = DECK_FOLDER / deck.legality.name.lower() / deck.clan.name.lower()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{deck.id}.json"
    path.write_text(deck.to_json())
    return path


def main():
    logging.basicConfig(level=logging.DEBUG)

    target_legalities = ["emperor", "onyx", "20f"]

    for legality_short in target_legalities:
        legality_ = next(
            (
                x
                for x in legalities
                if legality_short.lower()
                in {x.name.lower(), x.acronym.lower(), x.short.lower()}
            ),
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
            _save_deck(deck)


def main_two_decks():
    logging.basicConfig(level=logging.DEBUG)

    deck1, deck2 = generate_two_decks()

    for deck in (deck1, deck2):
        deck.show()
        path = _save_deck(deck)
        logging.info("Saved deck to %s", path)


if __name__ == "__main__":
    main()
