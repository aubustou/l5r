from __future__ import annotations

from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Open:</b> Give a Province +3 strength. Destroy this Holding."
Collapsing_Bridge = Holding(
    card_id=1429,
    title="Collapsing Bridge",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold.<br><b>Limited:</b> Give your target Personality +2F. Destroy this Holding."
Frontline_Encampment = Holding(
    card_id=2706,
    title="Frontline Encampment",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
