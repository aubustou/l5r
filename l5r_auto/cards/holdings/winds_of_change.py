from __future__ import annotations

from l5r_auto.keywords import Farm, Retainer
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Ashigaru_Fort = Holding(
    card_id=614,
    title="Ashigaru Fort",
    gold_cost=2,
    keywords=[Farm],
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
Reserve_Commander = Holding(
    card_id=6267,
    title="Reserve Commander",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
