from __future__ import annotations

from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Vengeful_Populace = Holding(
    card_id=9138,
    title="Vengeful Populace",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
