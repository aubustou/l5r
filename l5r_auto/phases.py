from __future__ import annotations

import abc
import logging
import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.abilities import Ability, RecruitAction

if TYPE_CHECKING:
    from .play import Game
    from .player import Player


@dataclass(kw_only=True)
class Step:
    game: Game

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass


@dataclass(kw_only=True)
class StartOfGame(Step):
    """After a game of L5R starts, follow steps A through F in sequence."""

    game: Game

    class ShowStrongholds(Step):
        """A. All players show their Strongholds and Sensei (if any), and start with the Stronghold
        and any Sensei in play. Each player begins with his or her Family Honor stat at his or
        her Stronghold’s Starting Honor, modied by his or her Sensei.
        """

        def start(self):
            for player in self.game.players:
                player.set_starting_honor()

    class DetermineStartingPlayer(Step):
        """B. The starting player is the player with the highest Family Honor.

        If one or more players are tied in Family Honor, they decide who goes first randomly, such as by
        rolling dice or flipping a coin. The starting player uses the “going first” side of his or
        her Stronghold, and the others turn their Stronghold to the “going second” side.
        """

        def start(self):
            highest_honor = max(x.honor for x in self.game.players)
            self.game.starting_player = random.choice(
                [x for x in self.game.players if x.honor == highest_honor]
            )

            logging.info("Starting player: %s", self.game.starting_player.name)

            sorted_list = []
            current_player = self.game.starting_player

            while True:
                sorted_list.append(current_player)
                if (player_to_the_right := current_player.right_to) is None:
                    break

                # Move to the player on the right
                current_player = player_to_the_right

                # Stop if we have looped back to the start
                if current_player == self.game.starting_player:
                    break

            self.game.players = sorted_list
            logging.info("Player order:")
            for player in self.game.players:
                logging.info("\t%s", player.name)

    class ShuffleDecks(Step):
        """C. All players shuffle both their decks separately. Players should offer their decks to
        the other players for further shuing or cutting."""

        def start(self):
            for player in self.game.players:
                player.shuffle_decks()

    class CreateProvinces(Step):
        """D. Players place their decks and create four Provinces, then ll each one from left to
        right with a card from the top of their Dynasty deck."""

        def start(self):
            for player in self.game.players:
                player.create_provinces()

    class DrawCards(Step):
        """E. All players draw five Fate cards simultaneously."""

        def start(self):
            for player in self.game.players:
                player.draw_hand()

    class PlayGame(Step):
        """F. Play begins.

        The starting player becomes the active player and takes a turn
        sequence (Action Phase through Dynasty Phase). When his or her turn has ended, the
        next player’s turn, in turn order, begins, and he or she becomes the active player. This
        continues until one player has won the game, at which point the game ends
        immediately.
        When the starting player is determined, he or she is also considered the active player
        for purposes of things that happen before the first turn begins.
        """

        def start(self):
            logging.info("Finished start of game: %s", self.game.id)

    steps = [
        ShowStrongholds,
        DetermineStartingPlayer,
        ShuffleDecks,
        CreateProvinces,
        DrawCards,
        PlayGame,
    ]

    def start(self):
        for step in self.steps:
            step(game=self.game).start()


@dataclass(kw_only=True)
class TurnSequences(Step):
    """A game of L5R is divided into turns.

    Beginning with the starting player, and continuing
    in turn order (that is, proceeding to the left), each player takes a turn.
    At any time after the start of the game, turn order starts with the active player and
    continues clockwise, to each player’s left.
    """

    def start(self):
        for player in self.game.players:
            self.game.current_player = player
            self.game.take_turn(number=1, active_player=player)


@dataclass(kw_only=True)
class Phase(Step):
    turn: Turn
    active_player: Player

    abilities: list[Ability] = field(default_factory=list)

    def start(self):
        logging.info(
            "%s: Starting phase: %s", self.active_player.name, self.__class__.__name__
        )


# Turn Sequence
# Start Phase - Straighten Phase - Event Phase - Action Phase - Attack/Battle Phase (optional) - Dynasty Phase - Discard Phase - Draw Phase - End Phase
@dataclass(kw_only=True)
class StartPhase(Phase):
    pass


@dataclass(kw_only=True)
class StraightenPhase(Phase):
    pass


@dataclass(kw_only=True)
class EventPhase(Phase):
    pass


@dataclass(kw_only=True)
class ActionPhase(Phase):
    pass


@dataclass(kw_only=True)
class AttackPhase(Phase):
    optional: bool = field(default=True, init=False)
    current_segment: AttackPhaseSegment | None = field(default=None, init=False)


@dataclass(kw_only=True)
class DynastyPhase(Phase):
    abilities = [
        RecruitAction(),
    ]

    def __post_init__(self, *args, **kwargs):
        self.abilities.extend([RecruitAction()])


@dataclass(kw_only=True)
class DiscardPhase(Phase):
    pass


@dataclass(kw_only=True)
class DrawPhase(Phase):
    pass


@dataclass(kw_only=True)
class EndPhase(Phase):
    pass


@dataclass(kw_only=True)
class Turn:
    game: Game
    number: int
    active_player: Player

    phases = [
        StartPhase,
        StraightenPhase,
        EventPhase,
        ActionPhase,
        AttackPhase,
        DynastyPhase,
        DiscardPhase,
        DrawPhase,
        EndPhase,
    ]

    def start(self):
        logging.info("%s: Starting turn #%d", self.active_player.name, self.number)
        for phase in self.phases:
            self.game.current_phase = phase(
                game=self.game, turn=self, active_player=self.active_player
            )
            self.game.current_phase.start()

    def to_dict(self):
        return {
            "number": self.number,
            "active_player": self.active_player.name,
        }


# Attack phase
@dataclass(kw_only=True)
class AttackPhaseSegment(Phase):
    pass


@dataclass(kw_only=True)
class Declaration(AttackPhaseSegment):
    pass


@dataclass(kw_only=True)
class Maneuver(AttackPhaseSegment):
    pass


@dataclass(kw_only=True)
class Fight(AttackPhaseSegment):
    pass


# Battles
@dataclass(kw_only=True)
class BattlePhase(Phase):
    pass


@dataclass(kw_only=True)
class EngageSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class CombatSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class ResolutionSegment(BattlePhase):
    pass


@dataclass(kw_only=True)
class AftermathSegment(BattlePhase):
    pass
