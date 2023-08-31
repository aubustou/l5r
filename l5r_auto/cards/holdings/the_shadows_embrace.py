from __future__ import annotations

from l5r_auto.keywords import Mine, Retainer
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Platinum_Mine = Holding(
    card_id=9798,
    title="Platinum Mine",
    gold_cost=6,
    gold_production="5",
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
SmallTime_Bully = Holding(
    card_id=9800,
    title="Small-Time Bully",
    gold_cost=2,
    keywords=[Retainer],
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
