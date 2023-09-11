from __future__ import annotations

from l5r_auto.keywords import Temple
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>:bow::</b> When paying for a Monk, he enters play for 3 less Gold."
Temple_of_Harmony = Holding(
    card_id=7874,
    title="Temple of Harmony",
    gold_cost=2,
    keywords=[Temple],
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
    gold_production="2",
)
