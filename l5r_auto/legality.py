from __future__ import annotations


class Legality:
    name: str
    acronym: str
    short: str


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


class TwentyFestivalsEdition(Legality):
    name = "twenty festivals edition"
    acronym = "20f"
    short = "twenty festivals"


class OnyxEdition(Legality):
    name = "onyx edition"
    acronym = "oe"
    short = "onyx"


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
