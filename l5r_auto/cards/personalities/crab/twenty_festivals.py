from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    Commander,
    Conqueror,
    Daimyo,
    Earth,
    Experienced,
    Jade,
    Loyal,
    Magistrate,
    Resilient,
    Samurai,
    Shugenja,
    Siege,
    SoulOf,
    Tactician,
    Unique,
    WitchHunter,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Battle, :bow::</b> Reduce a target enemy Follower or Personality's Force by Taisho's Force."
Hida_Taisho = Personality(
    card_id=12081,
    title="Hida Taisho",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle.)</i><br><b>Battle:</b> Fear equal to Zaiburo's Force minus 1."
Hida_Zaiburo = Personality(
    card_id=12082,
    title="Hida Zaiburo",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Conqueror, Berserker],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Engage:</b> If Raikohime is opposed, discard a card to make the enemy leader either discard a Battle Strategy, or show you his hand if it does not have one."
Hiruma_Raikohime = Personality(
    card_id=12083,
    title="Hiruma Raikohime",
    force=5,
    chi=3,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Before you Proclaim Burei, increase the Honor gain to equal the number of your Fortifications in play, up to 5."
Kaiu_Burei = Personality(
    card_id=12084,
    title="Kaiu Burei",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> If Daikohime is defending, Ranged 3 Attack. After this destroys a card, gain 1 Honor."
Kaiu_Daikohime = Personality(
    card_id=12085,
    title="Kaiu Daikohime",
    force=0,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt:</b> After the action Recruits a Fortification from a Province, refill it face-up. <br><b>Battle:</b> Ranged 3 Attack with +1 strength for each Fortification at this battlefield."
Kaiu_Watsuki_Experienced = Personality(
    card_id=12086,
    title="Kaiu Watsuki",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[Loyal, Tactician, Unique, Daimyo, Experienced("1"), Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i>"
Kuni_Chutsu = Personality(
    card_id=12087,
    title="Kuni Chutsu",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Battle, :bow::</b> Melee 3 Attack, or Melee 4 Attack if the target is Shadowlands <i>(Destroy a target enemy Follower or Personality without Followers with Force equal to or lower than the Melee Attack's strength)</i>."
Kuni_Harakibi = Personality(
    card_id=12088,
    title="Kuni Harakibi",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Earth, Shugenja, WitchHunter],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Interrupt:</b> If the action is Earth, negate the next straightening <i>(this turn)</i> of each card it bows.<br><b>Earth Unstoppable Battle:</b> Bow a target enemy card that is Dragon Clan, Gaijin, Shadowlands, or has no attachments."
Kuni_Renyu_Experienced_3 = Personality(
    card_id=12089,
    title="Kuni Renyu",
    force=5,
    chi=5,
    personal_honor=3,
    gold_cost=11,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[
        Experienced("3"),
        Loyal,
        Unique,
        Daimyo,
        Earth,
        Jade,
        Magistrate,
        Shugenja,
        WitchHunter,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Earth Battle, :g*::</b> Equip a target Follower in your hand to your target Personality."
Kuni_Yairao = Personality(
    card_id=12090,
    title="Kuni Yairao",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Commander, Earth, Shugenja, SoulOf("Kuni Iyedo")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
