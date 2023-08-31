from __future__ import annotations

from l5r_auto.keywords import Farm, GeishaHouse, Market
from l5r_auto.legality import (
    DiamondEdition,
    EmperorEdition,
    GoldEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

House_of_the_Red_Lotus = Holding(
    card_id=3501,
    title="House of the Red Lotus",
    gold_cost=2,
    keywords=[GeishaHouse],
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
Rice_Paddy = Holding(
    card_id=6314,
    title="Rice Paddy",
    gold_cost=2,
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Trading_Grounds = Holding(
    card_id=8710,
    title="Trading Grounds",
    gold_cost=2,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        GoldEdition,
        JadeEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
