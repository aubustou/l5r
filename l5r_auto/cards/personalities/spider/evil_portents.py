from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Conqueror,
    Destined,
    Duelist,
    Experienced,
    Infiltrator,
    Ninja,
    Nonhuman,
    Ogre,
    Resilient,
    Samurai,
    Shadowlands,
    Undead,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Daigotsu_Aimaro = Personality(
    card_id=12482,
    title="Daigotsu Aimaro",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Duelist, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Daigotsu_Endo_Experienced = Personality(
    card_id=12483,
    title="Daigotsu Endo",
    force=4,
    chi=0,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Destined, Experienced("1"), Nonhuman, Samurai, Shadowlands, Undead],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Daigotsu_Yuhmi_Experienced_2 = Personality(
    card_id=12484,
    title="Daigotsu Yuhmi",
    force=6,
    chi=2,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Experienced("2"), Unique, Infiltrator, Nonhuman, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Goju_Iaitsu = Personality(
    card_id=12485,
    title="Goju Iaitsu",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Goju_Toriken = Personality(
    card_id=12486,
    title="Goju Toriken",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Conqueror, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Hikayo = Personality(
    card_id=12487,
    title="Hikayo",
    force=5,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Resilient, Nonhuman, Ogre, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
