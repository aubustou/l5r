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

"This Holding has +1GP when it pays for a single attachment only."
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
"After you Recruit this Holding, if you control a Courtier or Magistrate, you may dishonor a Personality. <br><b>:bow::</b> Produce 2 Gold."
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
    gold_production="2",
)
