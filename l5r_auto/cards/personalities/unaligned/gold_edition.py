from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Commander, Nonhuman, Shadowlands, Undead, Zombie
from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After you Recruit Noekam, lose 5 Honor. Noekam's Undead Followers have +1F. <br><b>Battle:</b> Fear with strength equal to the number of Undead cards in this unit."
Noekam = Personality(
    card_id=5611,
    title="Noekam",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Commander, Nonhuman, Shadowlands, Undead, Zombie],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
        ModernEdition,
    ],
)
