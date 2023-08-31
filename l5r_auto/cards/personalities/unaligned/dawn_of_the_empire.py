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

Hatsu_Suru_no_Oni = Personality(
    id=5734,
    title="Hatsu Suru no Oni",
    force=4,
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
