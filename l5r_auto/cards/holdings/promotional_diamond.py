from __future__ import annotations

from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Battle, :bow::</b> Bow your target unbowed Follower or Item. Bow a target enemy Personality without attachments."
Vengeful_Populace = Holding(
    card_id=9138,
    title="Vengeful Populace",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
