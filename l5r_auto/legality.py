from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from .clans import (
    Clan,
    CrabClan,
    CraneClan,
    DragonClan,
    LionClan,
    MantisClan,
    NagaFaction,
    PhoenixClan,
    ScorpionClan,
    SpiderClan,
    UnicornClan,
    clans,
)


@dataclass(frozen=True, kw_only=True)
class GameRules:
    # Victory / end conditions
    honor_victory_threshold: int = 40
    max_number_of_turns: int = 50

    # Player starting state
    minimum_honor: int = -20
    starting_hand_size: int = 5
    max_hand_size: int = 8
    starting_number_of_provinces: int = 4
    successive_battle_actions: int = 1

    # Deck construction
    max_copies_per_card: int = 3
    min_gold_producers: int = 6

    # Deck composition targets
    deck_personalities: int = 12
    deck_holdings: int = 11
    deck_events: int = 2
    deck_strategies: int = 10
    deck_followers: int = 5
    deck_items: int = 5


class Legality:
    name: str
    acronym: str
    short: str

    legal_clans: list[type[Clan]] = clans
    rules: ClassVar[GameRules] = GameRules()


class ImperialEdition(Legality):
    name = "imperial edition"
    acronym = "ie"
    short = "imperial"


class JadeEdition(Legality):
    name = "jade edition"
    acronym = "je"
    short = "jade"


class GoldEdition(Legality):
    name = "gold edition"
    acronym = "ge"
    short = "gold"


class DiamondEdition(Legality):
    name = "diamond edition"
    acronym = "de"
    short = "diamond"


class LotusEdition(Legality):
    name = "lotus edition"
    acronym = "le"
    short = "lotus"


class SamuraiEdition(Legality):
    name = "samurai edition"
    acronym = "se"
    short = "samurai"


class CelestialEdition(Legality):
    name = "celestial edition"
    acronym = "ce"
    short = "celestial"


class EmperorEdition(Legality):
    name = "emperor edition"
    acronym = "ee"
    short = "emperor"


_ivory_rules = GameRules(
    starting_hand_size=6,
    deck_personalities=10,
    deck_holdings=9,
    deck_events=1,
    deck_strategies=8,
    deck_followers=4,
    deck_items=4,
)


class IvoryEdition(Legality):
    name = "ivory edition"
    acronym = "ie"
    short = "ivory"

    legal_clans = [
        CrabClan,
        CraneClan,
        DragonClan,
        LionClan,
        MantisClan,
        PhoenixClan,
        ScorpionClan,
        SpiderClan,
        UnicornClan,
    ]
    rules: ClassVar[GameRules] = _ivory_rules


class TwentyFestivalsEdition(Legality):
    name = "twenty festivals edition"
    acronym = "20f"
    short = "twenty festivals"

    legal_clans = [
        CrabClan,
        CraneClan,
        DragonClan,
        LionClan,
        MantisClan,
        PhoenixClan,
        ScorpionClan,
        SpiderClan,
        UnicornClan,
    ]
    rules: ClassVar[GameRules] = _ivory_rules


class OnyxEdition(Legality):
    name = "onyx edition"
    acronym = "oe"
    short = "onyx"

    legal_clans = [
        CrabClan,
        CraneClan,
        DragonClan,
        LionClan,
        NagaFaction,
        PhoenixClan,
        ScorpionClan,
        SpiderClan,
        UnicornClan,
    ]


class ModernEdition(Legality):
    name = "modern edition"
    acronym = "me"
    short = "modern"


legalities = [
    ImperialEdition,
    JadeEdition,
    GoldEdition,
    DiamondEdition,
    LotusEdition,
    SamuraiEdition,
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    TwentyFestivalsEdition,
    OnyxEdition,
    ModernEdition,
]
