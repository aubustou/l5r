"""Self-play harness: run N games between two policies and tally outcomes.

Usage::

    python -m l5r_auto.ai.harness --p1 heuristic --p2 random --n 200 --seed 42

Requires pre-built decks in ``l5r_auto/decks/`` (run ``build_deck`` first).
"""

from __future__ import annotations

import argparse
import copy
import logging
import random
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from l5r_auto.ai.heuristic_policy import HeuristicPolicy
from l5r_auto.ai.policy import Policy
from l5r_auto.ai.random_policy import RandomPolicy
from l5r_auto.deck import Deck
from l5r_auto.errors import (
    EndOfDynastyDeckError,
    EndOfFateDeckError,
    HonorVictory,
    MaximumNumberOfTurnsReached,
    ProvinceConquestVictory,
)
from l5r_auto.play import DECK_PATH, Game
from l5r_auto.player import Player

POLICY_FACTORIES: dict[str, Callable[[random.Random], Policy]] = {
    "random": lambda rng: RandomPolicy(rng=rng),
    "heuristic": lambda _rng: HeuristicPolicy(),
}


@dataclass
class MatchResult:
    p1_name: str
    p2_name: str
    games: int
    p1_wins: int = 0
    p2_wins: int = 0
    draws: int = 0
    outcomes: Counter = field(default_factory=Counter)

    @property
    def p1_win_rate(self) -> float:
        decisive = self.p1_wins + self.p2_wins
        return self.p1_wins / decisive if decisive else 0.0

    def summary(self) -> str:
        return (
            f"{self.p1_name} vs {self.p2_name}: "
            f"{self.p1_wins}W / {self.p2_wins}L / {self.draws}D "
            f"over {self.games} games "
            f"({self.p1_win_rate:.1%} win-rate). "
            f"Outcomes: {dict(self.outcomes)}"
        )


def _load_deck_pool() -> list[tuple[Path, Deck]]:
    pool: list[tuple[Path, Deck]] = []
    for path in DECK_PATH.rglob("*.json"):
        try:
            pool.append((path, Deck.from_json(path.read_text())))
        except Exception as e:
            logging.debug("Skipping unreadable deck %s: %s", path, e)
    return pool


def _pick_deck_pair(
    pool: list[tuple[Path, Deck]], rng: random.Random
) -> tuple[Deck, Deck]:
    by_legality: dict[str, list[tuple[Path, Deck]]] = {}
    for path, deck in pool:
        by_legality.setdefault(deck.legality.name, []).append((path, deck))
    eligible = [decks for decks in by_legality.values() if len(decks) >= 2]
    if not eligible:
        raise RuntimeError("No legality has at least 2 decks in decks/.")
    decks = rng.choice(eligible)
    a, b = rng.sample(decks, 2)
    return copy.deepcopy(a[1]), copy.deepcopy(b[1])


def run_match(
    p1_factory: Callable[[random.Random], Policy],
    p2_factory: Callable[[random.Random], Policy],
    p1_name: str,
    p2_name: str,
    n_games: int,
    seed: int | None = None,
) -> MatchResult:
    """Run ``n_games`` between two policies and tally outcomes."""
    rng = random.Random(seed)
    pool = _load_deck_pool()
    if not pool:
        raise RuntimeError(
            "No decks found in decks/. Run `build_deck` first to generate some."
        )

    result = MatchResult(p1_name=p1_name, p2_name=p2_name, games=n_games)

    for i in range(n_games):
        # Seed the stdlib random too: deck shuffles and starting-player
        # tie-breaks still use the module global.
        random.seed(rng.random())

        deck1, deck2 = _pick_deck_pair(pool, rng)
        pol1 = p1_factory(random.Random(rng.random()))
        pol2 = p2_factory(random.Random(rng.random()))

        player1 = Player(name=f"P1-{p1_name}", deck=deck1, policy=pol1)
        player2 = Player(name=f"P2-{p2_name}", deck=deck2, policy=pol2)
        game = Game(players=[player1, player2], legality=deck1.legality)

        winner, outcome = _play_one(game, player1, player2)
        result.outcomes[outcome] += 1
        if winner is player1:
            result.p1_wins += 1
        elif winner is player2:
            result.p2_wins += 1
        else:
            result.draws += 1

        if (i + 1) % 10 == 0:
            logging.info(
                "[%d/%d] %s %dW  %s %dW  draws %d",
                i + 1,
                n_games,
                p1_name,
                result.p1_wins,
                p2_name,
                result.p2_wins,
                result.draws,
            )

    return result


def _play_one(game: Game, p1: Player, p2: Player):
    try:
        game.start()
    except HonorVictory as e:
        return e.winner, "honor"
    except ProvinceConquestVictory as e:
        return e.winner, "province_conquest"
    except MaximumNumberOfTurnsReached:
        return _decide_by_honor(p1, p2, "turn_cap")
    except EndOfDynastyDeckError:
        return _decide_by_honor(p1, p2, "dynasty_deckout")
    except EndOfFateDeckError:
        return _decide_by_honor(p1, p2, "fate_deckout")
    # Should not fall through: game.start() always raises one of the above.
    return None, "unknown"


def _decide_by_honor(p1: Player, p2: Player, outcome: str):
    if p1.honor > p2.honor:
        return p1, outcome
    if p2.honor > p1.honor:
        return p2, outcome
    return None, outcome


def main() -> None:
    parser = argparse.ArgumentParser(description="Self-play harness for l5r_auto.")
    parser.add_argument(
        "--p1", default="heuristic", choices=sorted(POLICY_FACTORIES)
    )
    parser.add_argument("--p2", default="random", choices=sorted(POLICY_FACTORIES))
    parser.add_argument("--n", type=int, default=50)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.WARNING if args.quiet else logging.INFO,
        format="%(message)s",
    )

    # Silence the engine's chatty DEBUG logs in harness runs; keep harness-level info.
    logging.getLogger("l5r_auto").setLevel(logging.WARNING)

    result = run_match(
        POLICY_FACTORIES[args.p1],
        POLICY_FACTORIES[args.p2],
        p1_name=args.p1,
        p2_name=args.p2,
        n_games=args.n,
        seed=args.seed,
    )
    print(result.summary())


if __name__ == "__main__":
    main()
