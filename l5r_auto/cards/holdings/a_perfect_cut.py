from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 1 Gold. <br><b>Battle/Open, :bow::</b> Target your Personality. Negate all current and future <i>(this turn)</i> Chi penalties on him from other players' cards, and tokens they created."
Tea_House = Holding(
    card_id=7852,
    title="Tea House",
    gold_cost=1,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="1",
)
