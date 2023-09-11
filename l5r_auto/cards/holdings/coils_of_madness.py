from __future__ import annotations

from l5r_auto.keywords import Temple
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"This Holding has +2GP when it pays for a single attachment only."
Colonial_Temple = Holding(
    card_id=10433,
    title="Colonial Temple",
    gold_cost=3,
    keywords=[Temple],
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
