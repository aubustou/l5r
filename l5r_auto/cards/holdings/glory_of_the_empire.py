from __future__ import annotations

from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

House_of_Exotic_Goods = Holding(
    card_id=3493,
    title="House of Exotic Goods",
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
)
