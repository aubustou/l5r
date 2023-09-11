from __future__ import annotations

from l5r_auto.keywords import Market, Retainer, Village
from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Battle/Open, :bow::</b> Target a Personality. Negate future Fear effects on his unit <i>(this turn)</i>."
Clear_Water_Village = Holding(
    card_id=1418,
    title="Clear Water Village",
    gold_cost=2,
    keywords=[Village],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Battle, :bow::</b> Target another player's Personality at any location who was moved home from the current battlefield. Straighten his unit and move him there."
Roaming_Caravan = Holding(
    card_id=6369,
    title="Roaming Caravan",
    gold_cost=2,
    keywords=[Market, Retainer],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
