from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    ClanChampion,
    Conqueror,
    Courtier,
    Experienced,
    Kensai,
    Loyal,
    Monk,
    Orator,
    Paragon,
    Samurai,
    Shadowlands,
    Shugenja,
    SoulOf,
    TheShadowEmperor,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Daigotsu_Geiko = Personality(
    id=11220,
    title="Daigotsu Geiko",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Samurai, SoulOf("Daigotsu Keigo")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Daigotsu_Kanpeki_the_Shadow_Emperor_Experienced_3 = Personality(
    id=11221,
    title="Daigotsu Kanpeki, the Shadow Emperor",
    force=6,
    chi=5,
    personal_honor=0,
    gold_cost=12,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[
        Conqueror,
        Experienced("3"),
        Kensai,
        Loyal,
        Unique,
        ClanChampion,
        Monk,
        Paragon,
        Samurai,
        TheShadowEmperor,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Daigotsu_Konishi = Personality(
    id=11222,
    title="Daigotsu Konishi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Daigotsu_Onosaka = Personality(
    id=11223,
    title="Daigotsu Onosaka",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Daigotsu_Roburo = Personality(
    id=11224,
    title="Daigotsu Roburo",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Paragon, Samurai, Shadowlands, SoulOf("Daigotsu Bundoru")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Hiyamako = Personality(
    id=11225,
    title="Hiyamako",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=2,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Susumu_Neya = Personality(
    id=11226,
    title="Susumu Neya",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=1,
    clan=[SpiderClan],
    keywords=[Courtier, Orator],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Susumu_Yanada = Personality(
    id=11227,
    title="Susumu Yanada",
    force=0,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Tairao = Personality(
    id=11228,
    title="Tairao",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Shadowlands, Shugenja, SoulOf("Chuda Rintaro")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
