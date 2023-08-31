from __future__ import annotations

from l5r_auto.keywords import Retainer
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Yasuki_Trader = Holding(
    card_id=9468,
    title="Yasuki Trader",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
