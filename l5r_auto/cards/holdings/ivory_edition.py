from __future__ import annotations

from l5r_auto.keywords import GeishaHouse, Port, Temple
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

Brilliant_Cascade_Inn = Holding(
    card_id=11140,
    title="Brilliant Cascade Inn",
    gold_cost=1,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Deep_Harbor = Holding(
    card_id=11141,
    title="Deep Harbor",
    gold_cost=1,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Secluded_Shrine = Holding(
    card_id=11144,
    title="Secluded Shrine",
    gold_cost=1,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
