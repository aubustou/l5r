from __future__ import annotations

from l5r_auto.keywords import Dojo
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold.<br><b>:bow::</b> When paying for a Follower, it enters play for 3 less Gold."
Akodo_Dojo = Holding(
    card_id=201,
    title="Akodo Dojo",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, DiamondEdition, ModernEdition],
    gold_production="2*",
)
