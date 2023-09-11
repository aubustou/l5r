from __future__ import annotations

from l5r_auto.keywords import Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"After you Recruit this Holding, lose 1 Honor. <br><b>:bow::</b> Produce 2 Gold. <br><b>Battle/Open, :bow::</b> Fear effects from cards <i>(now)</i> in a target Personality's unit have +1 strength."
Carrions_Breath = Holding(
    card_id=1222,
    title="Carrion's Breath",
    gold_cost=2,
    keywords=[Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold. <br><b>:bow::</b> When paying for an action on a Strategy, it costs 3 less Gold."
Kaeru_Contractor = Holding(
    card_id=4091,
    title="Kaeru Contractor",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
