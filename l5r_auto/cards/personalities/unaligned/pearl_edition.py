from __future__ import annotations

from l5r_auto.clans import NinjaFaction, Unaligned
from l5r_auto.keywords import Ninja
from l5r_auto.legality import (
    ImperialEdition,
    JadeEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Ninja_Shapeshifter = Personality(
    id=5579,
    title="Ninja Shapeshifter",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=10,
    honor_requirement=None,
    clan=[Unaligned, NinjaFaction],
    keywords=[Ninja],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        ImperialEdition,
        JadeEdition,
        OnyxEdition,
        ModernEdition,
    ],
)
