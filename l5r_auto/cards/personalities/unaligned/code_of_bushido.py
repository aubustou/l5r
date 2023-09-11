from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Nonhuman, Oni, Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After you Recruit Minikui, lose 5 Honor.<br><b>Battle:</b> Fear with a strength equal to your target Oni's Chi."
Minikui_no_Oni = Personality(
    card_id=5059,
    title="Minikui no Oni",
    force=6,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
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
)
