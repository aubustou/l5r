from __future__ import annotations

from l5r_auto.keywords import Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Carrions_Breath = Holding(
    card_id=1222,
    title="Carrion's Breath",
    gold_cost=2,
    keywords=[Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Kaeru_Contractor = Holding(
    card_id=4091,
    title="Kaeru Contractor",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
