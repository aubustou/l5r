from __future__ import annotations

from l5r_auto.clans import (
    BrotherhoodOfShinsei,
    NinjaFaction,
    ShadowlandsFaction,
    SpiderClan,
)
from l5r_auto.keywords import (
    Assassin,
    Conqueror,
    Courtier,
    Kensai,
    Monk,
    Naval,
    Ninja,
    Reserve,
    Resilient,
    Samurai,
    Shadowlands,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Daigotsu_Jemaru = Personality(
    card_id=11604,
    title="Daigotsu Jemaru",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Reserve, Resilient, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Goju_Saido = Personality(
    card_id=11605,
    title="Goju Saido",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Assassin, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Marimako = Personality(
    card_id=11606,
    title="Marimako",
    force=3,
    chi=1,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=0,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Conqueror, Kensai, Naval, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Susumu_Jaru = Personality(
    card_id=11607,
    title="Susumu Jaru",
    force=1,
    chi=1,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Susumu_Tanjin = Personality(
    card_id=11608,
    title="Susumu Tanjin",
    force=0,
    chi=2,
    personal_honor=1,
    gold_cost=2,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yasi = Personality(
    card_id=11609,
    title="Yasi",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Resilient, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
