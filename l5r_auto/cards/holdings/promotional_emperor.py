from __future__ import annotations

from l5r_auto.keywords import Kharmic, Market
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Open, :bow::</b> Straighten your target Courtier."
Jiramus_Court = Holding(
    card_id=10189,
    title="Jiramu's Court",
    gold_cost=2,
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
Traveling_Market = Holding(
    card_id=10571,
    title="Traveling Market",
    gold_cost=3,
    keywords=[Kharmic, Market],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
