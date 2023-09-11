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

"After a Dark Virtue, Fear, or Maho action resolves, if Geiko is at the current battlefield, give him +1F."
Daigotsu_Geiko = Personality(
    card_id=11220,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Reduce your Honor losses from your cards by 1, to a minimum of 1. After your Fear action at Kanpeki's battlefield bows a Follower, destroy it.<br><b>Battle:</b> Take two additional Battle actions."
Daigotsu_Kanpeki_the_Shadow_Emperor_Experienced_3 = Personality(
    card_id=11221,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Give a target enemy Follower or Personality -2F."
Daigotsu_Konishi = Personality(
    card_id=11222,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> Give one of the action's Fear effects +1 strength."
Daigotsu_Onosaka = Personality(
    card_id=11223,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Fear 4 <i>(Bow a target enemy Follower, or Personality without Followers, with 4 or lower Force)</i>."
Daigotsu_Roburo = Personality(
    card_id=11224,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i></i>"
Hiyamako = Personality(
    card_id=11225,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Political Open, :bow::</b> Give a target Personality <i>(in play)</i> +1PH or -1PH. <br><b>Favor Political Interrupt, :bow::</b> Discard the Imperial Favor to increase or decrease a Proclaim Honor gain by 1."
Susumu_Neya = Personality(
    card_id=11226,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"You are considered to have +5 Family Honor when Lobbying checks Honor.<br><b>Interrupt, :bow::</b> The Fear action destroys any cards it bows."
Susumu_Yanada = Personality(
    card_id=11227,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Open:</b> Target another player's Personality. After each time he assigns this turn, give him -2F/-1C and <b>Shadowlands</b> <i>(this turn)</i>."
Tairao = Personality(
    card_id=11228,
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
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
