from __future__ import annotations

from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Limited:</b> Put one or more face-up cards in your Provinces at the bottom of your deck <i>(and refill the Provinces)</i>. Turn all cards in your Provinces face-up. Destroy this Holding."
House_of_Exotic_Goods = Holding(
    card_id=3493,
    title="House of Exotic Goods",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
