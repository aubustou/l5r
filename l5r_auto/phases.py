from __future__ import annotations

import abc
import itertools
import logging
import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.abilities import (
    Ability,
    AttachFollowerAbility,
    AttachItemAbility,
    CycleAction,
    KharmicAction,
    PlayStrategyAbility,
    RecruitAction,
)
from l5r_auto.ai.policy import (
    KIND_ACTION_ROUND,
    KIND_ATTACK_TARGET,
    KIND_DISCARD_HAND,
    PASS,
    Decision,
    Option,
)
from l5r_auto.cards.events.common import Event
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.errors import (
    EndOfFateDeckError,
    HonorVictory,
    MaximumNumberOfTurnsReached,
    ProvinceConquestVictory,
)

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

    def _run_action_round(
        self,
        abilities: list[Ability],
        active_types: set[str],
        other_types: set[str],
    ):
        """Run an action round with player alternation.

        Players take turns choosing one action. The active player may use
        action types in active_types; other players may use types in
        other_types. The round ends when all players pass consecutively.
        """
        for ability in abilities:
            ability.on_start_phase(self.game)

        # Build turn order starting with active player
        players = list(self.game.players)
        start_idx = players.index(self.active_player)
        ordered = players[start_idx:] + players[:start_idx]

        consecutive_passes = 0
        player_idx = 0
        max_actions = 500  # Safety limit

        while consecutive_passes < len(ordered) and player_idx < max_actions:
            current = ordered[player_idx % len(ordered)]
            allowed = active_types if current == self.active_player else other_types

            took_action = self._try_player_action(current, abilities, allowed)

            if took_action:
                consecutive_passes = 0
            else:
                consecutive_passes += 1

            player_idx += 1

    def legal_actions(
        self,
        player: Player,
        abilities: list[Ability],
        allowed_types: set[str],
    ) -> list[tuple[Ability, object]]:
        """Enumerate every (ability, target) pair the player can legally take.

        Side-effect-free — used by :meth:`_try_player_action` to pose a
        Decision to the policy, and will be the single expansion function
        for any future tree-search policy.
        """
        pairs: list[tuple[Ability, object]] = []
        for ability in abilities:
            if not self._ability_type_allowed(ability, allowed_types):
                continue
            if ability.done_once_per_turn and not ability.repeatable:
                continue
            for entity in ability.gather_legal_target_entities(self.game, player):
                if not ability.can_pay(self.game, entity):
                    continue
                pairs.append((ability, entity))
        return pairs

    def _try_player_action(
        self,
        player: Player,
        abilities: list[Ability],
        allowed_types: set[str],
    ) -> bool:
        """Ask the player's policy to pick one legal action (or pass).

        Returns True if an action was actually taken.
        """
        pairs = self.legal_actions(player, abilities, allowed_types)
        if not pairs:
            return False

        options = [
            Option(
                id=f"act:{ability.__class__.__name__}:{getattr(entity, 'id', entity)}",
                payload=(ability, entity),
            )
            for ability, entity in pairs
        ]
        options.append(PASS)
        decision = Decision(
            kind=KIND_ACTION_ROUND,
            player=player,
            options=options,
            context={
                "phase": self.__class__.__name__,
                "allowed_types": sorted(allowed_types),
            },
        )
        picked = player.policy.choose(decision, self.game)
        if not picked or picked[0] is PASS or picked[0].payload is None:
            return False

        ability, entity = picked[0].payload
        if not ability.pay_cost(self.game, entity):
            return False
        ability.get_effect(self.game, entity)
        if not ability.repeatable:
            ability.done_once_per_turn = True
        return True

    @staticmethod
    def _ability_type_allowed(ability: Ability, allowed_types: set[str]) -> bool:
        """Check if an ability's declared type is within the allowed set."""
        for t in allowed_types:
            if getattr(ability, t, False):
                return True
        return False


# Turn Sequence (Twenty Festivals rules):
# 1. Action Phase (straighten, reveal provinces, event activation, action round)
# 2. Attack Phase (optional: declaration, maneuvers, fight battles)
# 3. Dynasty Phase (recruit/discard action round, draw 1 card, discard to max hand size)


@dataclass(repr=False, kw_only=True)
class ActionPhase(Phase):
    """Action Phase: straighten cards, reveal provinces, activate events, then action round.

    At the start, straighten all bowed cards and reveal face-down Province cards.
    Events in provinces are activated (discarded). Then an action round of
    Limited actions (active player only) and Open actions (all players).
    """

    def __post_init__(self, *args, **kwargs):
        self.abilities = [
            CycleAction(),
            KharmicAction(),
            PlayStrategyAbility(),
            AttachFollowerAbility(),
            AttachItemAbility(),
        ]

    def _straighten(self):
        """Straighten all bowed cards at the start of the Action Phase."""
        logging.info(
            "%s: Straightening cards in play.",
            self.active_player.name,
        )
        self.active_player.stronghold_entity.straighten()
        if self.active_player.sensei_entity:
            self.active_player.sensei_entity.straighten()
        for card in self.active_player.play_area:
            card.straighten()

    def _reveal_provinces(self):
        """Reveal face-down cards in provinces."""
        logging.info("%s: Revealing provinces", self.active_player.name)
        for province in self.active_player.provinces:
            for card in province.dynasty_cards:
                if card.face_down:
                    card.turn_face_up()

    def _activate_events(self):
        """Activate face-up events in provinces (they are discarded on use)."""
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

    def _action_round(self):
        """Action round: active player Limited + Open, other players Open."""
        self._run_action_round(
            self.abilities,
            active_types={"limited", "open"},
            other_types={"open"},
        )

    def _start(self):
        self._straighten()
        self._reveal_provinces()
        self._activate_events()
        self._action_round()


@dataclass(repr=False, kw_only=True)
class AttackPhase(Phase):
    """Attack Phase: Declaration, Maneuvers, Fight (Engage, Combat, Resolution, Aftermath).

    Per Twenty Festivals rules:
    - Attacker declares which province to attack and assigns unbowed Personalities
    - Defender assigns unbowed Personalities to defend
    - Force is calculated from unbowed Personalities and their attachments
    - Resolution: loser's units are destroyed; winner gains 2 Honor per enemy card destroyed
    - Ties: both sides destroy each other
    - Province destroyed only if attacker Force > defender Force + Province Strength
    - After resolution: surviving attackers bow and return home (Conqueror skips bowing)
    """

    optional: bool = field(default=True, init=False)

    def _get_unbowed_personalities(self, player) -> list[PersonalityEntity]:
        return [
            e
            for e in player.play_area
            if isinstance(e, PersonalityEntity) and e.face_up and not e.bowed
        ]

    def _total_force(self, personalities: list[PersonalityEntity]) -> int:
        """Calculate total force of personalities and their unbowed attachments."""
        total = 0
        for p in personalities:
            if not p.bowed:
                total += getattr(p, "force", 0)
            for e in p.owner.play_area:
                if getattr(e, "attached_to", None) is p:
                    force_val = getattr(e, "force", "0")
                    try:
                        total += int(force_val)
                    except (ValueError, TypeError):
                        pass
        return total

    def _get_province_strength(self, province) -> int:
        """Get Province Strength from the defender's Stronghold."""
        defender = province.player
        return getattr(defender.stronghold, "province_strength", 0)

    def _has_keyword(self, entity, keyword_class) -> bool:
        return any(
            (isinstance(kw, type) and issubclass(kw, keyword_class))
            or kw is keyword_class
            for kw in entity.keywords
        )

    def _start(self):
        """Execute the Attack Phase: Declaration → Maneuvers → Fight."""
        attacker = self.active_player
        defenders = [p for p in self.game.players if p is not attacker]
        if not defenders:
            return
        defender = defenders[0]

        # --- Declaration Segment ---
        attacking_units = self._get_unbowed_personalities(attacker)
        if not attacking_units:
            logging.info("%s: No unbowed personalities to attack with.", attacker.name)
            return

        # Ask attacker's policy which province to attack (or to pass).
        valid_provinces = [prov for prov in defender.provinces if prov.dynasty_cards]
        if not valid_provinces:
            logging.info("%s: No valid provinces to attack.", attacker.name)
            return
        options = [
            Option(id=f"province:{i}", payload=prov)
            for i, prov in enumerate(valid_provinces)
        ]
        options.append(PASS)
        decision = Decision(
            kind=KIND_ATTACK_TARGET,
            player=attacker,
            options=options,
            context={
                "defender": defender,
                "attacker_force_approx": self._total_force(attacking_units),
            },
        )
        picked = attacker.policy.choose(decision, self.game)
        if not picked or picked[0] is PASS or picked[0].payload is None:
            logging.info("%s: Declines to attack.", attacker.name)
            return
        target_province = picked[0].payload

        logging.info(
            "%s: Declares attack on province %s with %d personalities.",
            attacker.name,
            target_province,
            len(attacking_units),
        )

        # --- Maneuvers Segment ---
        defending_units = self._get_unbowed_personalities(defender)
        if defending_units:
            logging.info(
                "%s: Assigns %d personalities to defend.",
                defender.name,
                len(defending_units),
            )

        # --- Fight: Engage Segment (placeholder for Engage actions) ---

        # --- Fight: Combat Segment ---
        attacker_force = self._total_force(attacking_units)
        defender_force = self._total_force(defending_units)
        province_strength = self._get_province_strength(target_province)

        logging.info(
            "%s attacks province %s: attacker force %d vs defender force %d "
            "(province strength %d).",
            attacker.name,
            target_province,
            attacker_force,
            defender_force,
            province_strength,
        )

        # --- Fight: Resolution Segment ---
        if not defending_units:
            # Undefended province: destroyed if attacker force > province strength
            if attacker_force > province_strength:
                logging.info(
                    "%s: Undefended province — force %d > province strength %d.",
                    attacker.name,
                    attacker_force,
                    province_strength,
                )
                self._destroy_province(target_province, attacker, defender)
            else:
                logging.info(
                    "%s: Undefended province survives — force %d <= province strength %d.",
                    attacker.name,
                    attacker_force,
                    province_strength,
                )
        elif attacker_force > defender_force:
            # Attacker wins
            destroyed_count = self._destroy_units(defending_units)
            logging.info(
                "%s: Attacker wins battle (force %d > %d). Destroyed %d defender cards.",
                attacker.name,
                attacker_force,
                defender_force,
                destroyed_count,
            )
            # Winner gains 2 Honor per enemy card destroyed
            if destroyed_count > 0:
                honor_gain = 2 * destroyed_count
                attacker.honor += honor_gain
                logging.info(
                    "%s: Gains %d Honor for destroying %d enemy cards.",
                    attacker.name,
                    honor_gain,
                    destroyed_count,
                )
            # Check if province is destroyed (attacker force > defender force + province strength)
            if attacker_force > defender_force + province_strength:
                self._destroy_province(target_province, attacker, defender)
            else:
                logging.info(
                    "%s: Province survives — attacker force %d <= defender force %d + "
                    "province strength %d.",
                    attacker.name,
                    attacker_force,
                    defender_force,
                    province_strength,
                )
        elif defender_force > attacker_force:
            # Defender wins
            destroyed_count = self._destroy_units(attacking_units)
            logging.info(
                "%s: Defender wins battle (force %d > %d). Destroyed %d attacker cards.",
                defender.name,
                defender_force,
                attacker_force,
                destroyed_count,
            )
            if destroyed_count > 0:
                honor_gain = 2 * destroyed_count
                defender.honor += honor_gain
                logging.info(
                    "%s: Gains %d Honor for destroying %d enemy cards.",
                    defender.name,
                    honor_gain,
                    destroyed_count,
                )
        else:
            # Tie: both sides destroy each other
            attacker_destroyed = self._destroy_units(defending_units)
            defender_destroyed = self._destroy_units(attacking_units)
            logging.info(
                "Battle tied at force %d. Both sides destroyed "
                "(%d defender, %d attacker cards).",
                attacker_force,
                attacker_destroyed,
                defender_destroyed,
            )
            if attacker_destroyed > 0:
                honor_gain = 2 * attacker_destroyed
                attacker.honor += honor_gain
                logging.info(
                    "%s: Gains %d Honor for destroying %d enemy cards in tie.",
                    attacker.name,
                    honor_gain,
                    attacker_destroyed,
                )
            if defender_destroyed > 0:
                honor_gain = 2 * defender_destroyed
                defender.honor += honor_gain
                logging.info(
                    "%s: Gains %d Honor for destroying %d enemy cards in tie.",
                    defender.name,
                    honor_gain,
                    defender_destroyed,
                )

        # --- Fight: Aftermath Segment ---
        self._return_home(attacking_units)

    def _destroy_units(self, units: list[PersonalityEntity]) -> int:
        """Destroy a list of units, respecting Resilient. Returns count destroyed."""
        destroyed = 0
        for entity in units[:]:
            if self._try_destroy(entity):
                destroyed += 1
        return destroyed

    def _try_destroy(self, entity: PersonalityEntity) -> bool:
        """Attempt to destroy a personality, respecting Resilient.

        Returns True if the entity was actually destroyed.
        """
        from l5r_auto.keywords import Resilient

        resilient_used = getattr(entity, "_resilient_used", False)
        if self._has_keyword(entity, Resilient) and not resilient_used:
            logging.info(
                "%s: %s uses Resilient — bowed instead of destroyed.",
                entity.owner.name,
                entity.title,
            )
            entity._resilient_used = True
            entity.bow()
            return False
        else:
            entity.destroy()
            return True

    def _return_home(self, units: list[PersonalityEntity]):
        """Surviving attackers bow and return home. Conqueror skips bowing."""
        from l5r_auto.keywords import Conqueror
        from l5r_auto.locations import PlayArea

        for entity in units[:]:
            if entity.location is not PlayArea:
                continue  # Already destroyed/moved
            if self._has_keyword(entity, Conqueror):
                logging.info(
                    "%s: %s has Conqueror — returns home without bowing.",
                    entity.owner.name,
                    entity.title,
                )
            else:
                entity.bow()

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


@dataclass(repr=False, kw_only=True)
class DynastyPhase(Phase):
    """Dynasty Phase: recruit/discard action round, then draw 1 Fate card, discard to max hand size.

    Per Twenty Festivals rules, at the end of the Dynasty Phase:
    - Draw 1 Fate card
    - If hand exceeds max hand size (8), discard down to max
    """

    def __post_init__(self, *args, **kwargs):
        self.abilities = [
            RecruitAction(),
        ]

    def _dynasty_action_round(self):
        """Dynasty action round: active player takes Dynasty actions, others Open."""
        self._run_action_round(
            self.abilities,
            active_types={"dynasty"},
            other_types={"open"},
        )

    def _end_of_turn_draw(self):
        """At the end of the Dynasty Phase, draw 1 Fate card."""
        player = self.active_player
        logging.info(
            "%s: Drawing 1 fate card (end of turn).",
            player.name,
        )
        try:
            player.draw_fate_card()
        except EndOfFateDeckError:
            logging.info("%s: Fate deck is empty.", player.name)

    def _end_of_turn_discard(self):
        """After drawing, discard down to max hand size — policy picks which."""
        player = self.active_player
        excess = len(player.hand) - player.max_hand_size
        if excess <= 0:
            return

        options = [
            Option(id=f"hand:{c.id}:{c.title}", payload=c) for c in player.hand
        ]
        decision = Decision(
            kind=KIND_DISCARD_HAND,
            player=player,
            options=options,
            min_picks=excess,
            max_picks=excess,
            context={"max_hand_size": player.max_hand_size},
        )
        picked = player.policy.choose(decision, self.game)

        # Defensive: if the policy returned the wrong number of picks, pad
        # or truncate to `excess` so the rules invariant holds.
        picked_cards = [opt.payload for opt in picked if opt.payload is not None]
        if len(picked_cards) < excess:
            remaining = [c for c in player.hand if c not in picked_cards]
            picked_cards.extend(remaining[: excess - len(picked_cards)])
        picked_cards = picked_cards[:excess]

        for card in picked_cards:
            logging.info(
                "%s: Discarding %s from hand (over max hand size %d).",
                player.name,
                card.title,
                player.max_hand_size,
            )
            card.discard()

    def _start(self):
        self._dynasty_action_round()
        self._end_of_turn_draw()
        self._end_of_turn_discard()


@dataclass(repr=False, kw_only=True)
class Turn:
    """A turn in L5R consists of:
    - Honor Victory check at start of turn (>= 40)
    - Action Phase
    - Attack Phase (optional)
    - Dynasty Phase (includes end-of-turn draw and discard)
    - Dishonor Loss check at end of turn (<= -20)
    """

    game: Game
    number: int
    active_player: Player

    phases = [
        ActionPhase,
        AttackPhase,
        DynastyPhase,
    ]

    def _check_honor_victory(self):
        """Honor Victory: a player wins by starting his or her turn on 40+ Family Honor."""
        player = self.active_player
        if player.honor >= self.game.rules.honor_victory_threshold:
            other_players = [p for p in self.game.players if p is not player]
            logging.info(
                "%s: Wins by Honor Victory (%d >= %d) at start of turn.",
                player.name,
                player.honor,
                self.game.rules.honor_victory_threshold,
            )
            raise HonorVictory(winner=player, loser=other_players[0])

    def _check_dishonor_loss(self):
        """Dishonor Loss: if a player's Honor is -20 or below at the end of his turn, he loses."""
        player = self.active_player
        if player.honor <= self.game.rules.minimum_honor:
            other_players = [p for p in self.game.players if p is not player]
            logging.info(
                "%s: Loses by Dishonor (%d <= %d) at end of turn.",
                player.name,
                player.honor,
                self.game.rules.minimum_honor,
            )
            raise HonorVictory(winner=other_players[0], loser=player)

    def start(self):
        logging.info("%s: Starting turn #%d", self.active_player.name, self.number)

        # Honor Victory check at start of turn
        self._check_honor_victory()

        # Run the three canonical phases
        for phase in self.phases:
            self.game.current_phase = phase(
                game=self.game, turn=self, active_player=self.active_player
            )
            self.game.current_phase.start()

        # Dishonor Loss check at end of turn
        self._check_dishonor_loss()

    def to_dict(self):
        return {
            "number": self.number,
            "active_player": self.active_player.name,
        }
