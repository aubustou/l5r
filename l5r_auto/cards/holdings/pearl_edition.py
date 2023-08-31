from __future__ import annotations

from l5r_auto.legality import (
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

School_of_Wizardry = Holding(
    card_id=6494,
    title="School of Wizardry",
    gold_cost=7,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
        JadeEdition,
        ModernEdition,
        ModernEdition,
    ],
)
