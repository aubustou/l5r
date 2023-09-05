from __future__ import annotations

import itertools
import logging
import random
import time
import uuid
from dataclasses import field
from pathlib import Path
from typing import TYPE_CHECKING, Type

from l5r_auto.locations import PlayArea
from l5r_auto.utils import dataclass_ as dataclass

from .deck import Deck
from .legality import Legality
from .phases import StartOfGame, Turn, TurnSequences

if TYPE_CHECKING:
    from .cards import Entity
    from .models import GameReport
    from .phases import Phase, Step
    from .player import Player

DECK_PATH = Path(__file__).parent / "decks"
REPORT_FOLDER = Path(__file__).parent / "reports"


@dataclass
class Game:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    players: list[Player]
    legality: Type[Legality]

    current_player: Player | None = None
    current_phase: Phase | None = None
    current_step: Step | None = None

    starting_player: Player | None = field(init=False)

    phases: list[Phase] = field(default_factory=list)
    turns: list[Turn] = field(default_factory=list)

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

    @property
    def current_turn(self) -> Turn:
        return self.turns[-1]

    @property
    def entities(self) -> list[Entity]:
        return [x for player in self.players for x in player.entities]

    def start(self):
        logging.info("Starting game: %s", self.id)
        for step in self.steps:
            self.current_step = step(game=self)
            self.current_step.start()

    def take_turn(self, number: int, active_player: Player):
        turn = Turn(game=self, number=number, active_player=active_player)
        self.turns.append(turn)
        turn.start()

    def report(self):
        id = str(self.id)
        report_folder = REPORT_FOLDER / id[:2]
        report_folder.mkdir(parents=True, exist_ok=True)
        report_file = report_folder / f"{id}.json"

        report = GameReport(
            id=self.id,
            players=[x.report() for x in self.players],
        )
        report_file.write_text(self.to_json())

    def end_report(self):
        for player in self.players:
            logging.info("Cards on play area:")
            for entity in sorted(player.entities, key=lambda x: x.__class__.__name__):
                if entity.location is PlayArea:
                    logging.info("\t%s", entity.title)
            logging.info("Total force on play area:")
            logging.info(
                "\t%s: %d",
                player.name,
                sum(
                    x.force
                    for x in player.entities
                    if x.location is PlayArea and x.face_up and hasattr(x, "force")
                ),
            )


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting L5R Auto")
    start_time = time.time()

    # TODO: Add command line arguments
    # TODO: Add name handling
    name = None

    deck_paths = list(DECK_PATH.rglob("*.json"))
    logging.info("Found %d decks", len(deck_paths))
    random.shuffle(deck_paths)

    from .player import Player

    for paths in itertools.pairwise(deck_paths):
        players = []
        decks = []
        legalities = set()

        for path in paths:
            logging.info("Loading deck: %s", path)
            deck = Deck.from_json(path.read_text())
            logging.info("Loaded deck %s:", deck.id)
            decks.append(deck)
            legalities.add(deck.legality)

        if len(legalities) > 1:
            raise ValueError("Decks must have the same legality")
        legality = legalities.pop()

        for deck in decks:
            logging.info("\tDeck version: %s", deck.version)
            logging.info("\tDeck stronghold: %s", deck.stronghold.title)

            player = Player(name=name or "", deck=deck)
            logging.info("Created player: %s", player.name)
            players.append(player)

        game = Game(players=players, legality=legality)
        logging.info("Created game: %s", game.id)

        game.start()
        logging.info("Finished game: %s", game.id)
        game.end_report()
        break

    logging.info("Finished in %1.2f seconds", time.time() - start_time)


if __name__ == "__main__":
    main()
