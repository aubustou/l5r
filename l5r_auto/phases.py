from __future__ import annotations

import abc
import itertools
import logging
import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.abilities import (
    ABILITIES,
    Ability,
    AttachFollowerAbility,
    AttachItemAbility,
    DynastyDiscardAction,
    PlayStrategyAbility,
    RecruitAction,
)
from l5r_auto.cards.events.common import Event
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.errors import (
    EndOfFateDeckError,
    HonorVictory,
    MaximumNumberOfTurnsReached,
    ProvinceConquestVictory,
)
from l5r_auto.locations import PlayArea

if TYPE_CHECKING:
    from .play import Game
    from .player import Player


@dataclass(repr=False, kw_only=True)
class Step:
    game: Game

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass


@dataclass(repr=False, kw_only=True)
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
                player.show_stronghold()
                player.show_sensei()

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

            if len(sorted_list) != len(self.game.players):
                raise ValueError("Player list is not the same length as the game.")

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


@dataclass(repr=False, kw_only=True)
class TurnSequences(Step):
    """A game of L5R is divided into turns.

    Beginning with the starting player, and continuing
    in turn order (that is, proceeding to the left), each player takes a turn.
    At any time after the start of the game, turn order starts with the active player and
    continues clockwise, to each player’s left.
    """

    def start(self):
        for turn_number, player in enumerate(
            itertools.cycle(self.game.players), start=1
        ):
            if turn_number >= self.game.rules.max_number_of_turns:
                logging.info("Reached maximum number of turns: %d", turn_number)
                raise MaximumNumberOfTurnsReached()

            self.game.current_player = player
            self.game.take_turn(number=turn_number, active_player=player)


@dataclass(repr=False, kw_only=True)
class Phase(Step):
    turn: Turn
    active_player: Player

    abilities: list[Ability] = field(default_factory=list)

    def start(self):
        logging.info(
            "%s: Starting phase: %s", self.active_player.name, self.__class__.__name__
        )
        self._start()

    def _start(self):
        pass


# Turn Sequence
# Start Phase - Straighten Phase - Event Phase - Action Phase - Attack/Battle Phase (optional) - Dynasty Phase - Discard Phase - Draw Phase - End Phase
@dataclass(repr=False, kw_only=True)
class StartPhase(Phase):
    def _start(self):
        for ability in ABILITIES.values():
            ability.on_start_phase(self.game)

        logging.info("%s: Revealing provinces", self.active_player.name)
        for province in self.active_player.provinces:
            for card in province.dynasty_cards:
                if card.face_down:
                    card.turn_face_up()


@dataclass(repr=False, kw_only=True)
class StraightenPhase(Phase):
    def _start(self):
        logging.info(
            "%s: Straightening cards in play.",
            self.active_player.name,
        )
        self.active_player.stronghold_entity.straighten()
        if self.active_player.sensei_entity:
            self.active_player.sensei_entity.straighten()
        for card in self.active_player.play_area:
            card.straighten()


@dataclass(repr=False, kw_only=True)
class EventPhase(Phase):
    def _start(self):
        for province in self.active_player.provinces:
            for card in province.dynasty_cards[:]:
                if isinstance(card, Event) and card.face_up:
                    logging.info(
                        "%s: Activating event: %s",
                        self.active_player.name,
                        card.title,
                    )
                    card.discard()
                    province.dynasty_cards.remove(card)

            if not province.dynasty_cards:
                province.fill()


@dataclass(repr=False, kw_only=True)
class ActionPhase(Phase):
    def __post_init__(self, *args, **kwargs):
        self.abilities = [
            PlayStrategyAbility(),
            AttachFollowerAbility(),
            AttachItemAbility(),
        ]

    def _start(self):
        for ability in self.abilities:
            for entity in ability.gather_legal_target_entities(
                self.game, self.active_player
            ):
                if not ability.pay_cost(self.game, entity):
                    continue
                ability.get_effect(self.game, entity)


@dataclass(repr=False, kw_only=True)
class AttackPhase(Phase):
    optional: bool = field(default=True, init=False)
    current_segment: AttackPhaseSegment | None = field(default=None, init=False)

    def _get_personalities(self, player) -> list[PersonalityEntity]:
        return [
            e for e in player.play_area
            if isinstance(e, PersonalityEntity) and e.face_up
        ]

    def _total_force(self, personalities: list[PersonalityEntity]) -> int:
        total = 0
        for p in personalities:
            total += getattr(p, "force", 0)
            # Add force from attached followers/items
            for e in p.owner.play_area:
                if getattr(e, "attached_to", None) is p:
                    force_val = getattr(e, "force", "0")
                    try:
                        total += int(force_val)
                    except (ValueError, TypeError):
                        pass
        return total

    def _start(self):
        attacker = self.active_player
        defenders = [p for p in self.game.players if p is not attacker]
        if not defenders:
            return
        defender = defenders[0]

        unbowed_attackers = [
            e for e in self._get_personalities(attacker) if not e.bowed
        ]
        if not unbowed_attackers:
            logging.info("%s: No unbowed personalities to attack with.", attacker.name)
            return

        # Choose a random face-up province to attack
        valid_provinces = [
            prov for prov in defender.provinces if prov.dynasty_cards
        ]
        if not valid_provinces:
            logging.info("%s: No valid provinces to attack.", attacker.name)
            return
        target_province = random.choice(valid_provinces)

        # Bow all unbowed attackers
        for p in unbowed_attackers:
            p.bow()
        attacker_force = self._total_force(unbowed_attackers)

        # Defender bows all unbowed personalities
        unbowed_defenders = [
            e for e in self._get_personalities(defender) if not e.bowed
        ]
        for p in unbowed_defenders:
            p.bow()
        defender_force = self._total_force(unbowed_defenders)

        logging.info(
            "%s attacks province %s with force %d vs defender force %d.",
            attacker.name,
            target_province,
            attacker_force,
            defender_force,
        )

        if not unbowed_defenders:
            # Undefended attack: destroy province directly
            self._destroy_province(target_province, attacker, defender)
        elif attacker_force > defender_force:
            # Attacker wins: destroy defending personalities and the province
            logging.info(
                "%s: Attacker wins battle (force %d > %d). Destroying defenders and province.",
                attacker.name,
                attacker_force,
                defender_force,
            )
            for p in unbowed_defenders:
                self._destroy_with_resilient(p)
            self._destroy_province(target_province, attacker, defender)
        else:
            # Defender wins: destroy all attacking personalities
            logging.info(
                "%s: Defender wins battle (force %d >= %d). Destroying attackers.",
                defender.name,
                defender_force,
                attacker_force,
            )
            for p in unbowed_attackers:
                self._destroy_with_resilient(p)

    def _destroy_province(self, province, attacker, defender):
        logging.info(
            "%s: Province %s is destroyed.",
            attacker.name,
            province,
        )
        for card in province.dynasty_cards[:]:
            card.discard()
            province.dynasty_cards.remove(card)
        defender.remaining_provinces -= 1
        logging.info(
            "%s has %d province(s) remaining.",
            defender.name,
            defender.remaining_provinces,
        )
        if defender.remaining_provinces <= 0:
            raise ProvinceConquestVictory(winner=attacker, loser=defender)

    def _destroy_with_resilient(self, entity: PersonalityEntity):
        from l5r_auto.keywords import Resilient

        resilient_used = getattr(entity, "_resilient_used", False)
        has_resilient = any(
            isinstance(kw, type) and issubclass(kw, Resilient)
            or kw is Resilient
            for kw in entity.keywords
        )
        if has_resilient and not resilient_used:
            logging.info(
                "%s: %s uses Resilient — bowed instead of destroyed.",
                entity.owner.name,
                entity.title,
            )
            entity._resilient_used = True
            entity.bow()
        else:
            entity.destroy()


@dataclass(repr=False, kw_only=True)
class DynastyPhase(Phase):
    def __post_init__(self, *args, **kwargs):
        self.abilities = [
            RecruitAction(),
        ]

    def _start(self):
        # TODO: Here to add some IA logic
        for ability in self.abilities:
            for entity in ability.gather_legal_target_entities(
                self.game, self.active_player
            ):
                if not ability.pay_cost(self.game, entity):
                    continue

                ability.get_effect(self.game, entity)


@dataclass(repr=False, kw_only=True)
class DiscardPhase(Phase):
    def _start(self):
        player = self.active_player
        while len(player.hand) > player.hand_size:
            card = random.choice(player.hand)
            logging.info(
                "%s: Discarding %s from hand (over hand size).",
                player.name,
                card.title,
            )
            card.discard()


@dataclass(repr=False, kw_only=True)
class DrawPhase(Phase):
    def _start(self):
        player = self.active_player
        cards_to_draw = max(0, player.hand_size - len(player.hand))
        logging.info(
            "%s: Drawing %d fate card(s).",
            player.name,
            cards_to_draw,
        )
        for _ in range(cards_to_draw):
            try:
                player.draw_fate_card()
            except EndOfFateDeckError:
                logging.info("%s: Fate deck is empty.", player.name)
                break


@dataclass(repr=False, kw_only=True)
class EndPhase(Phase):
    def _start(self):
        for player in self.game.players:
            other_players = [p for p in self.game.players if p is not player]
            if player.honor >= self.game.rules.honor_victory_threshold:
                logging.info(
                    "%s: Wins by honor (%d).",
                    player.name,
                    player.honor,
                )
                raise HonorVictory(winner=player, loser=other_players[0])
            if player.honor < 0:
                logging.info(
                    "%s: Loses by dishonor (%d).",
                    player.name,
                    player.honor,
                )
                raise HonorVictory(winner=other_players[0], loser=player)


@dataclass(repr=False, kw_only=True)
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
@dataclass(repr=False, kw_only=True)
class AttackPhaseSegment(Phase):
    pass


@dataclass(repr=False, kw_only=True)
class Declaration(AttackPhaseSegment):
    pass


@dataclass(repr=False, kw_only=True)
class Maneuver(AttackPhaseSegment):
    pass


@dataclass(repr=False, kw_only=True)
class Fight(AttackPhaseSegment):
    pass


# Battles
@dataclass(repr=False, kw_only=True)
class BattlePhase(Phase):
    pass


@dataclass(repr=False, kw_only=True)
class EngageSegment(BattlePhase):
    pass


@dataclass(repr=False, kw_only=True)
class CombatSegment(BattlePhase):
    pass


@dataclass(repr=False, kw_only=True)
class ResolutionSegment(BattlePhase):
    pass


@dataclass(repr=False, kw_only=True)
class AftermathSegment(BattlePhase):
    pass
