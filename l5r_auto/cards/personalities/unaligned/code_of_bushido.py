from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Nonhuman, Oni, Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Minikui_no_Oni = Personality(
    id=5059,
    title="Minikui no Oni",
    force=6,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=7,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        DiamondEdition,
        ModernEdition,
        IvoryEdition,
        LotusEdition,
        TwentyFestivalsEdition,
    ],
)
