from __future__ import annotations

from l5r_auto.keywords import Dojo, Imperial
from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Imperial_Dojo = Holding(
    card_id=3689,
    title="Imperial Dojo",
    gold_cost=2,
    keywords=[Dojo, Imperial],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
