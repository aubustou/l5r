from __future__ import annotations

from l5r_auto.keywords import Market, Retainer
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Wandering_Caravan = Holding(
    card_id=9203,
    title="Wandering Caravan",
    gold_cost=2,
    keywords=[Market, Retainer],
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
