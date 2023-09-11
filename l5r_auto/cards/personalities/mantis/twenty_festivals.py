from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Air,
    Commander,
    Daimyo,
    Experienced,
    Fire,
    Kensai,
    Magistrate,
    Naval,
    Reserve,
    Samurai,
    Shugenja,
    SoulOf,
    Thunder,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Your other Moshi Personalities in Ikako's army have +1F. After Ikako enters play, you may take an additional action.<br><b>Fire Battle:</b> Ranged Attack equal to 2 plus the number of other Personalities in this army."
Moshi_Ikako_Experienced = Personality(
    card_id=12128,
    title="Moshi Ikako",
    force=3,
    chi=5,
    personal_honor=3,
    gold_cost=11,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Naval, Reserve, Unique, Air, Daimyo, Experienced("1"), Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i>"
Moshi_Karuiko = Personality(
    card_id=12129,
    title="Moshi Karuiko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Shugenja, SoulOf("Moshi Kamiya"), Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 4 Attack. Bow the target if it is still in play."
Tsuruchi_Arayo = Personality(
    card_id=12130,
    title="Tsuruchi Arayo",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Samurai, SoulOf("Tsuruchi Amaya")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack. You may target a Mantis Clan Personality in one of your Provinces and reduce his Gold Cost by 2 <i>(this turn)</i>, to a minimum of 3."
Tsuruchi_Jinrai = Personality(
    card_id=12131,
    title="Tsuruchi Jinrai",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Magistrate, Samurai, SoulOf("Tsuruchi Jougo")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons. Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br><b>Battle:</b> Give a target enemy Personality -2F, or -3F if Juriken has a Gaijin or Peasant Weapon attached."
Yoritomo_Juriken = Personality(
    card_id=12132,
    title="Yoritomo Juriken",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br>While opposed, Kuniken has +1F for each of your Port Holdings, up to three Ports."
Yoritomo_Kuniken = Personality(
    card_id=12133,
    title="Yoritomo Kuniken",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Equipping Weapons is Battle/Open for you.<br><b>Battle:</b> Bow your target unbowed Weapon, then straighten it if it is Gaijin or Peasant. Destroy a target enemy attachment."
Yoritomo_Matsuo_Experienced = Personality(
    card_id=12134,
    title="Yoritomo Matsuo",
    force=4,
    chi=4,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Unique, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Economic Home Interrupt, :g2::</b> Give the action's Ranged Attacks +2 or -2 strength."
Yoritomo_Minoro = Personality(
    card_id=12135,
    title="Yoritomo Minoro",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons.)</i> <br><b>Battle:</b> Fear 2, with +2 strength if Nintai has a Gaijin or Peasant Weapon attached, and with +1 strength if her army has fewer units than the enemy army."
Yoritomo_Nintai = Personality(
    card_id=12136,
    title="Yoritomo Nintai",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons. Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i>"
Yoritomo_Saitsuko = Personality(
    card_id=12137,
    title="Yoritomo Saitsuko",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i>"
Yoritomo_Tsuhime = Personality(
    card_id=12138,
    title="Yoritomo Tsuhime",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Naval, Magistrate, Samurai, SoulOf("Yoritomo Eriko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt:</b> If the action is a Ranged Attack action, after it resolves, give your target Personality +2F."
Yoritomo_Waito = Personality(
    card_id=12139,
    title="Yoritomo Waito",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Commander, Samurai, SoulOf("Yoritomo Iwata")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
