from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    JadeEdition,
    LotusEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Kabuki_Theater_Troupe = Holding(
    card_id=4080,
    title="Kabuki Theater Troupe",
    gold_cost=3,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
