from __future__ import annotations

from l5r_auto.keywords import Retainer
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    LotusEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Honored_Sensei = Holding(
    card_id=3440,
    title="Honored Sensei",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
Puppet_Theater_Troupe = Holding(
    card_id=6101,
    title="Puppet Theater Troupe",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
