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

"Ninja Shapeshifter's Followers must be Ninja.<br><b>Ninja Battle/Open:</b> Ninja Shapeshifter copies a target Personality's Force, Chi, Personal Honor, or ability that does not copy abilities."
Ninja_Shapeshifter = Personality(
    card_id=5579,
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
