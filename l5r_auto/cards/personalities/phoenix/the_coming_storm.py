from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Conqueror,
    Experienced,
    Fire,
    Magistrate,
    Samurai,
    Shugenja,
    Unique,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to this battle.)</i><br><b>Air Tireless Open:</b> Straighten Genma."
Isawa_Genma = Personality(
    card_id=11758,
    title="Isawa Genma",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[Cavalry, Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Fire Battle:</b> Melee 2 Attack or Ranged 2 Attack.<br><b>Fire Engage:</b> Give your target Shugenja +1F."
Isawa_Kaname_Advisor_to_the_Ruby_Champion_Experienced = Personality(
    card_id=11759,
    title="Isawa Kaname, Advisor to the Ruby Champion",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=9,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Unique, Experienced("1"), Fire, Magistrate, Shugenja, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Air Battle:</b> Fear equal to Kido's Chi <i>(Bow a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Fear's strength)</i>."
Isawa_Kido = Personality(
    card_id=11760,
    title="Isawa Kido",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=8,
    clan=[PhoenixClan],
    keywords=[Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle. Shugenja may attach and cast Spells.)</i>"
Isawa_Muira = Personality(
    card_id=11761,
    title="Isawa Muira",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[Conqueror, Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i><br><b>Battle:</b> Fear equal to 1 plus the number of actions resolved from your Kiho and Spells this battle."
Shiba_Kakei = Personality(
    card_id=11762,
    title="Shiba Kakei",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Cavalry, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Target your Shugenja at any location. Give Yuuchi a Force bonus equal to the target's Chi. <br><b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>."
Shiba_Yuuchi = Personality(
    card_id=11763,
    title="Shiba Yuuchi",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
