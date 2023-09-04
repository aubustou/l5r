from __future__ import annotations

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


class Legality:
    name: str
    acronym: str
    short: str

    legal_clans: list[type[Clan]] = clans


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
