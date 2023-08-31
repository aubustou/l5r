from __future__ import annotations

from l5r_auto.clans import NagaFaction, Unaligned
from l5r_auto.keywords import Constrictor, Naga, Nonhuman
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Chaldera = Personality(
    id=1289,
    title="Chaldera",
    force=4,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=2,
    clan=[Unaligned, NagaFaction],
    keywords=[Constrictor, Naga, Nonhuman],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
