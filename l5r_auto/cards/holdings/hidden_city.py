from __future__ import annotations

from l5r_auto.keywords import Dojo
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Akodo_Dojo = Holding(
    card_id=201,
    title="Akodo Dojo",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, DiamondEdition, ModernEdition],
)
