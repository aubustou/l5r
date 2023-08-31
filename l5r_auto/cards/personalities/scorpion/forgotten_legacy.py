from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import BitterLies, Kensai, Loyal, Paragon, Samurai, Yojimbo
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Bayushi_Toshimo = Personality(
    id=916,
    title="Bayushi Toshimo",
    force=4,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[ScorpionClan],
    keywords=[Kensai, Loyal, BitterLies, Paragon, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[
        CelestialEdition,
        ModernEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
    ],
)
