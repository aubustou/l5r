from __future__ import annotations

from l5r_auto.keywords import Fudo, Jade, Mine, Pearl, PearlBed, Temple
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>Open, :bow::</b> A target Holding's abilities may not be used."
Coastal_Pearl_Bed = Holding(
    card_id=10615,
    title="Coastal Pearl Bed",
    gold_cost=2,
    keywords=[Pearl, PearlBed],
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
    gold_production="2",
)
"<b>Open, :bow::</b> Give a target Personality and each of his Followers Cavalry."
Fudoist_Temple = Holding(
    card_id=10609,
    title="Fudoist Temple",
    gold_cost=3,
    keywords=[Fudo, Temple],
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
    gold_production="3",
)
"When this Holding produces Gold, you may give it +1GP <i>(this turn)</i>; if you do, it will not straighten until after your next Action Phase."
Jade_Mine = Holding(
    card_id=10614,
    title="Jade Mine",
    gold_cost=2,
    keywords=[Jade, Mine],
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
    gold_production="2",
)
"Courtesy: When this Holding produces Gold, you may give it +1GP <i>(this turn)</i> and lose 2 Honor. <i>(Courtesy traits do not take effect if you went first.)</i>"
Slave_Pits = Holding(
    card_id=10611,
    title="Slave Pits",
    gold_cost=2,
    keywords=[Mine],
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
    gold_production="2",
)
