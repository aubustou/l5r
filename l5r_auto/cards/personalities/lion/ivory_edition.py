from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    ClanChampion,
    Deathseeker,
    Experienced,
    Loyal,
    Paragon,
    Samurai,
    Scout,
    SoulOf,
    Tactician,
    TheSteelLion,
    Unique,
    WarLeader,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"You may target defending Personalities with the rulebook Favor Political Battle action. After you destroy an enemy card during battle <i>(including resolution)</i>, gain 1 Honor.<br><b>Battle:</b> Give all your other attacking Lion Clan Samurai at Dairuko's battlefield +1F and +1PH."
Akodo_Dairuko_the_Steel_Lion_Experienced_2 = Personality(
    card_id=11178,
    title="Akodo Dairuko, the Steel Lion",
    force=4,
    chi=5,
    personal_honor=5,
    gold_cost=10,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[
        Experienced("2"),
        Loyal,
        Tactician,
        Unique,
        ClanChampion,
        Paragon,
        Samurai,
        TheSteelLion,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<i>(<b>Battle:</b> Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i>"
Akodo_Kenaro = Personality(
    card_id=11179,
    title="Akodo Kenaro",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Tactician, Samurai, SoulOf("Akodo Ijiasu"), WarLeader],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Battle:</b> Give a target enemy Follower or Personality -2F."
Ikoma_Ichimoko = Personality(
    card_id=11180,
    title="Ikoma Ichimoko",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Fear 2, or Fear 3 if you control a Terrain."
Ikoma_Yoshimoko = Personality(
    card_id=11181,
    title="Ikoma Yoshimoko",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=5,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Fear 3 <i>(Bow a target enemy Follower, or Personality without Followers, with 3 or lower Force)</i>."
Matsu_Agai = Personality(
    card_id=11182,
    title="Matsu Agai",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[LionClan],
    keywords=[Deathseeker, Samurai, SoulOf("Matsu Agoro")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Target another of your Lion Clan Personalities. Give Choiko a Force or Chi bonus equal to the target's Personal Honor."
Matsu_Choiko = Personality(
    card_id=11183,
    title="Matsu Choiko",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=8,
    clan=[LionClan],
    keywords=[Samurai, SoulOf("Matsu Ryoichi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Move home a target enemy unit."
Matsu_Morito = Personality(
    card_id=11185,
    title="Matsu Morito",
    force=4,
    chi=2,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=2,
    clan=[LionClan],
    keywords=[Deathseeker, Samurai, SoulOf("Matsu Sanraku")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Favor and Lobby actions cannot target Rutaro."
Matsu_Rutaro = Personality(
    card_id=11186,
    title="Matsu Rutaro",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Samurai, SoulOf("Matsu Turi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Tayuko has +2F while attacking."
Matsu_Tayuko = Personality(
    card_id=11187,
    title="Matsu Tayuko",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=3,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Samurai, SoulOf("Matsu Aoiko")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
