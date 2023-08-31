from __future__ import annotations

from l5r_auto.keywords import Market
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Counting_House = Holding(
    card_id=1528,
    title="Counting House",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Famous_Bazaar = Holding(
    card_id=2470,
    title="Famous Bazaar",
    gold_cost=2,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Secluded_Outpost = Holding(
    card_id=6535,
    title="Secluded Outpost",
    gold_cost=6,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
