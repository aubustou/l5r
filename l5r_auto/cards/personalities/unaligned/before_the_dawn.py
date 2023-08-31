from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Air, BatClan, Shugenja
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Komori_Taruko = Personality(
    card_id=4537,
    title="Komori Taruko",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=1,
    clan=[Unaligned],
    keywords=[Air, BatClan, Shugenja],
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
