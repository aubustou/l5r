from __future__ import annotations

import itertools
import logging
import random
import uuid
from pathlib import Path

from l5r_auto.deck import Deck
from l5r_auto.player import Game, Player

DECK_PATH = Path(__file__).parent / "decks"


def create_player(deck: Deck) -> Player:
    return Player(name=f"robotor-{uuid.uuid4()}", deck=deck)


def create_game(players: list[Player]) -> Game:
    return Game(players=players)


def load_deck(deck_path: Path) -> Deck:
    return Deck.from_json(deck_path.read_text())


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting L5R Auto")

    deck_paths = list(DECK_PATH.rglob("*.json"))
    logging.info("Found %d decks", len(deck_paths))
    random.shuffle(deck_paths)

    for paths in itertools.pairwise(deck_paths):
        players = []
        for path in paths:
            logging.info("Loading deck: %s", path)
            deck = load_deck(path)
            logging.info("Loaded deck %s:", deck.id)
            logging.info("\tDeck version: %s", deck.version)
            logging.info("\tDeck stronghold: %s", deck.stronghold.title)

            player = create_player(deck)
            logging.info("Created player: %s", player.name)
            players.append(player)

        game = create_game(players)
        logging.info("Created game: %s", game.id)

        game.start()


if __name__ == "__main__":
    main()
