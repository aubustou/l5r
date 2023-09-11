from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Destined,
    Duelist,
    Fire,
    LoveLetter,
    Naval,
    Nonhuman,
    Orochi,
    Samurai,
    ScionOfFlame,
    ScionOfTheSea,
    Shugenja,
    Water,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Ranged Attacks targeting Fujigawa have -1 strength if another player is Mantis Clan.<br>Courtesy: Abilities on Fujigawa's Spells have <b>Unstoppable</b>. <i>(Courtesy traits do not take effect if you went first. Other players cannot Interrupt Unstoppable actions.)</i>"
Isawa_Fujigawa = Personality(
    card_id=11916,
    title="Isawa Fujigawa",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Fire Interrupt:</b> After the action resolves, if it was Fire and bowed or destroyed any enemy cards, give your target Shugenja +2F."
Isawa_Nomura = Personality(
    card_id=11914,
    title="Isawa Nomura",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Fire, ScionOfFlame, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Air Open, :bow::</b> After the next time this phase another player's action targets one of your cards, negate its <i>(remaining)</i> effects."
Isawa_Tenkawa_the_Scholar = Personality(
    card_id=11915,
    title="Isawa Tenkawa, the Scholar",
    force=0,
    chi=5,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Air, LoveLetter, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Kyuji may only move to a battlefield if any enemy units are there. <i>(Assigning isn't moving.)</i><br><b>Water Battle:</b> If Kyuji has not moved to a battlefield this turn, give it +2F/-2C."
Kyuji = Personality(
    card_id=11917,
    title="Kyuji",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=9,
    clan=[PhoenixClan],
    keywords=[Cavalry, Naval, Nonhuman, Orochi, ScionOfTheSea, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card. Duelists win tied duels versus non-Duelists.)</i>"
Shiba_Kintaro_the_Remembered = Personality(
    card_id=11919,
    title="Shiba Kintaro, the Remembered",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Destined, Duelist, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Unstoppable Battle:</b> Give a target enemy Follower or Personality -1F, or -3F if you control a Lion Clan Personality or your Stronghold's Gold Production is 3. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Shiba_Koshiba = Personality(
    card_id=11918,
    title="Shiba Koshiba",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=1,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
