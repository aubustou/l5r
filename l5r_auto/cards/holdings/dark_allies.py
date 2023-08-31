from __future__ import annotations

from l5r_auto.keywords import Market, Retainer, Village
from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Clear_Water_Village = Holding(
    card_id=1418,
    title="Clear Water Village",
    gold_cost=2,
    keywords=[Village],
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
Roaming_Caravan = Holding(
    card_id=6369,
    title="Roaming Caravan",
    gold_cost=2,
    keywords=[Market, Retainer],
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
