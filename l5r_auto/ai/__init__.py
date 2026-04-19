"""Pluggable AI / policy layer for l5r_auto.

Every non-deterministic choice in the simulation path (attack target, recruit
target, gold payment, hand discard, action-round pick, follower/item target)
is posed to the active player's ``policy`` as a :class:`Decision`. A policy
returns one or more :class:`Option` objects, which the engine then applies.

This module is deliberately tiny and import-cheap so that engine modules can
import the decision types without pulling in any heavy AI code.
"""

from l5r_auto.ai.heuristic_policy import HeuristicPolicy
from l5r_auto.ai.policy import PASS, Decision, Option, Policy
from l5r_auto.ai.random_policy import RandomPolicy

__all__ = [
    "Decision",
    "Option",
    "Policy",
    "PASS",
    "RandomPolicy",
    "HeuristicPolicy",
]
