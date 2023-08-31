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
)
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
)
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
)
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
)
