from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Air, BatClan, Shugenja
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Komori_Taruko = Personality(
    id=4537,
    title="Komori Taruko",
    force=3,
    chi=4,
    honor_requirement=1,
    personal_honor=2,
    gold_cost=5,
    clan=[Unaligned],
    keywords=[Air, BatClan, Shugenja],
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
