from __future__ import annotations

from l5r_auto.keywords import Dojo, Imperial
from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Limited, :bow::</b> If you have two or fewer Provinces, discard any face-up Holdings in your Provinces, refilling those Provinces face-up."
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
