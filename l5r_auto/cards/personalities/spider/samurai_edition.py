from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Samurai, Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Daigotsu_Meguro = Personality(
    id=1745,
    title="Daigotsu Meguro",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        DiamondEdition,
        TwentyFestivalsEdition,
        SamuraiEdition,
        ModernEdition,
    ],
)
