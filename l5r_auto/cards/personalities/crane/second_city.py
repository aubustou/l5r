from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Courtier, Imperial
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Doji_Dainagon = Personality(
    id=2070,
    title="Doji Dainagon",
    force=1,
    chi=3,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Courtier, Imperial],
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
