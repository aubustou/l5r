from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Nonhuman, Samurai, Shadowlands, Undead
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After Zenshi enters play, lose 4 Honor. <br><b>Battle:</b> Give each Undead card in Zenshi's army +1F."
Daigotsu_Zenshi = Personality(
    card_id=1786,
    title="Daigotsu Zenshi",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Nonhuman, Samurai, Shadowlands, Undead],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        CelestialEdition,
        OnyxEdition,
        SamuraiEdition,
        ModernEdition,
    ],
)
