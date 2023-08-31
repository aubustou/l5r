from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Commander,
    Conqueror,
    Kensai,
    Monk,
    OrderOfTheSpider,
    Samurai,
    Shadowlands,
    SoulOf,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Daigotsu_Kendo = Personality(
    id=1736,
    title="Daigotsu Kendo",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Conqueror, Commander, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[ModernEdition, EmperorEdition, OnyxEdition, TwentyFestivalsEdition],
)
Sandayu = Personality(
    id=6467,
    title="Sandayu",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk, OrderOfTheSpider, SoulOf("Torao")],
    traits=[],
    abilities=[],
    legality=[ModernEdition, EmperorEdition, IvoryEdition, TwentyFestivalsEdition],
)
