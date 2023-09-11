from __future__ import annotations

from l5r_auto.keywords import Farm, Library, Market
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"You have +1 maximum hand size.<br><b>:bow::</b> Produce 2 Gold."
Farmers_Market = Holding(
    card_id=10033,
    title="Farmer's Market",
    gold_cost=2,
    keywords=[Farm, Market],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"After this Holding enters play from a Province, refill the Province face-up."
Small_Library = Holding(
    card_id=10038,
    title="Small Library",
    gold_cost=4,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
