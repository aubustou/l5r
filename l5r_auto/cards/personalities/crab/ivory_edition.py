from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    ClanChampion,
    Earth,
    Engineer,
    Experienced,
    Kensai,
    Loyal,
    Samurai,
    Scout,
    Shugenja,
    Siege,
    SoulOf,
    Tactician,
    TheLittleBear,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Battle, :bow::</b> Destroy one or more target enemy Followers with total Force less than or equal to Ayahi's Force."
Hida_Ayahi = Personality(
    card_id=11145,
    title="Hida Ayahi",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Berserker, Samurai, SoulOf("Hida Kashin")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Your Provinces have +1 strength. Fear effects, Melee Attacks, and Ranged Attacks targeting your Crab Clan Personalities in Kisada's army have -1 strength.<br><b>Tireless Battle/Open:</b> Straighten your target Follower or Personality."
Hida_Kisada_the_Little_Bear_Experienced = Personality(
    card_id=11146,
    title="Hida Kisada, the Little Bear",
    force=5,
    chi=5,
    personal_honor=3,
    gold_cost=12,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[
        Kensai,
        Loyal,
        Tactician,
        Unique,
        ClanChampion,
        Experienced("1"),
        Samurai,
        Siege,
        TheLittleBear,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Bow Reigoro's target unbowed Follower. The enemy leader targets and bows one of his unbowed Followers or Personalities."
Hida_Reigoro = Personality(
    card_id=11147,
    title="Hida Reigoro",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Samurai, SoulOf("Hida Renga")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Increase by 1 all Force bonuses Saiyuki receives <i><i>(for the duration of the Force bonus)</i></i>."
Hida_Saiyuki = Personality(
    card_id=11148,
    title="Hida Saiyuki",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Samurai, SoulOf("Kaiu Hisayuki")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Home Battle:</b> Target your Personality at any location. Switch his and Toranosuke's location. Straighten their units as they move."
Hida_Toranosuke = Personality(
    card_id=11149,
    title="Hida Toranosuke",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Target Fujito's Follower. Fear with strength equal to its Force <i>(Bow a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Fear's strength)</i>."
Hiruma_Fujito = Personality(
    card_id=11150,
    title="Hiruma Fujito",
    force=2,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Ranged 2 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>."
Hiruma_Itta = Personality(
    card_id=11151,
    title="Hiruma Itta",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Straighten your target Follower."
Hiruma_Tsurao = Personality(
    card_id=11152,
    title="Hiruma Tsurao",
    force=2,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Scout, SoulOf("Hiruma Todori")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Engage:</b> If your attacking army has fewer Personalities than the enemy army, the Defender chooses a number of units in his army equal to the difference, and they move home."
Kaiu_Nakagawa = Personality(
    card_id=11153,
    title="Kaiu Nakagawa",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[Engineer, Samurai, Siege, SoulOf("Kaiu Shoichi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Shugenja may attach and cast Spells.)</i></i><br>Negate Fear effects targeting cards in this unit. Ranged Attacks targeting cards in this unit have -2 strength."
Kuni_Tomokazu = Personality(
    card_id=11154,
    title="Kuni Tomokazu",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Earth, Shugenja, SoulOf("Kuni Takaniro")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
