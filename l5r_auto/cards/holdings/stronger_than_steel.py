from __future__ import annotations

from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you control a Courtier and the Imperial Favor."
Haiku_School = Holding(
    card_id=2944,
    title="Haiku School",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2*",
)
