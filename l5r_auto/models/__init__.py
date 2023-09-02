from __future__ import annotations

import itertools
import logging
import random
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Sequence, TypedDict

from typing_extensions import Required

from l5r_auto.errors import EndOfDynastyDeckError, EndOfFateDeckError
from l5r_auto.phases import StartOfGame, Turn, TurnSequences

from ..card import DynastyCard, FateCard
from ..locations import ProvinceLocation

if TYPE_CHECKING:
    from ..card import Ability
    from ..cards import Sensei, Stronghold
    from ..deck import Deck
    from ..phases import Phase, Step


class GameReport(TypedDict):
    id: uuid.UUID
    players: list[PlayerReport]


class PlayerReport(TypedDict):
    name: str
    deck: str
    stronghold: str
    sensei: str | None
    hand: list[str]
    provinces: list[ProvinceReport]
    dynasty_deck: list[str]
    fate_deck: list[str]
    dynasty_discard: list[str]
    fate_discard: list[str]
    removed_from_game: list[str]
    play_area: list[str]


class ProvinceReport(TypedDict):
    dynasty_cards: list[str]
    attachments: list[str]
    face_down: bool


class EntityReport(TypedDict, total=False):
    id: Required[str]
    title: Required[str]
    state: Required[list[str]]
    force: str
    chi: str
    honor_requirement: int | None
    gold_cost: str
    personal_honor: int
    keywords: list[str]
    abilities: list[str]
    traits: list[str]
