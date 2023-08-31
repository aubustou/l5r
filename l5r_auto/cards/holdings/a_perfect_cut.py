from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

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
)
