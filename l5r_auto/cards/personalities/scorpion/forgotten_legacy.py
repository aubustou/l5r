from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import BitterLies, Kensai, Loyal, Paragon, Samurai, Yojimbo
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Bayushi_Toshimo = Personality(
    card_id=916,
    title="Bayushi Toshimo",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, Loyal, BitterLies, Paragon, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
