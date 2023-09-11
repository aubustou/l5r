from __future__ import annotations

from l5r_auto.keywords import Retainer
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 5 Gold. <br><b>Political Limited, :bow::</b> If you control a Courtier or Magistrate, dishonor a target Personality."
Slanderer = Holding(
    card_id=7291,
    title="Slanderer",
    gold_cost=6,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
