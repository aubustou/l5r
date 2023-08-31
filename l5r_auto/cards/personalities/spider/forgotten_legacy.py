from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Ninja, Shadowlands, Shugenja, Unmaker
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Ninube_Shiho = Personality(
    id=5591,
    title="Ninube Shiho",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=4,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Ninja, Shadowlands, Shugenja, Unmaker],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        IvoryEdition,
        EmperorEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
    ],
)
