from __future__ import annotations

import logging
import random
from pathlib import Path

from l5r_auto.deck import Deck

DECK_PATH = Path(__file__).parent / "decks"


def load_deck(deck_path: Path) -> Deck:
    return Deck.from_json(deck_path.read_text())


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting L5R Auto")

    deck_paths = list(DECK_PATH.rglob("*.json"))
    logging.info("Found %d decks", len(deck_paths))
    random.shuffle(deck_paths)

    for path in deck_paths:
        logging.info("Loading deck: %s", path)
        deck = load_deck(path)
        logging.info("Loaded deck: %s", deck)


if __name__ == "__main__":
    main()
