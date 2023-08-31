from __future__ import annotations

from l5r_auto.keywords import Retainer
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Beautiful_Host = Holding(
    card_id=943,
    title="Beautiful Host",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        OnyxEdition,
        ModernEdition,
    ],
)
