from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Chieftain,
    Commander,
    Conqueror,
    Experienced,
    Imperial,
    Loyal,
    Magistrate,
    Samurai,
    Scout,
    Shugenja,
    SoulOf,
    Tactician,
    Unique,
    Water,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i>"
Iuchi_Daitoru = Personality(
    card_id=12181,
    title="Iuchi Daitoru",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Magistrate, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack. Straighten Aikenro if you have moved your Cavalry Personality to Aikenro's battlefield this turn."
Moto_Aikenro = Personality(
    card_id=12182,
    title="Moto Aikenro",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear equal to your target Follower's Force, with +1 strength if the Fear targets an enemy Infantry card."
Moto_Taigo_Shogun_Experienced_2 = Personality(
    card_id=12183,
    title="Moto Taigo, Shogun",
    force=4,
    chi=4,
    personal_honor=2,
    gold_cost=12,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[
        Cavalry,
        Conqueror,
        Experienced("2"),
        Tactician,
        Unique,
        Commander,
        Imperial,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i><br>After an action resolves, straighten each unit it moved into Yao-tsu's army."
Moto_Yaotsu = Personality(
    card_id=12184,
    title="Moto Yao-tsu",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=9,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Commander, Samurai, SoulOf("Moto Qu Yuan")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i>"
Moto_Zaitsuta = Personality(
    card_id=12185,
    title="Moto Zaitsuta",
    force=5,
    chi=3,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Chieftain, Samurai, SoulOf("Moto Zhijuan")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear 3 that may target a dishonorable Personality with Followers. If this bowed a dishonorable Personality, you may rehonor him to gain 1 Honor."
Shinjo_Hamura = Personality(
    card_id=12186,
    title="Shinjo Hamura",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt:</b> After your Battle action Recruits your Personality, take an additional action."
Shinjo_Jalendu = Personality(
    card_id=12187,
    title="Shinjo Jalendu",
    force=4,
    chi=2,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai, Scout, SoulOf("Shinjo Jalair")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle. Loyal Personalities will not join other Clans.)</i><br><b>Political Open, :bow::</b> Target a Personality. After the next time this turn he attacks you, dishonor him."
Shinjo_Jaoshen = Personality(
    card_id=12188,
    title="Shinjo Jao-shen",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Loyal, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"During an Attack Phase, if Nobunaga has not moved that phase, he has +1F and his printed Ranged Attack has +1 strength.<br><b>Battle, :bow::</b> Ranged 3 Attack."
Shinjo_Nobunaga = Personality(
    card_id=12189,
    title="Shinjo Nobunaga",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, SoulOf("Shinjo Xushen")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Other players' effects will not move dishonorable Personalities to oppose your Magistrates.<br><b>Battle:</b> Dishonor a target enemy Personality. You may take an additional action printed on your Magistrate or a card in his unit."
Shinjo_Taehyun_Experienced = Personality(
    card_id=12190,
    title="Shinjo Tae-hyun",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=8,
    clan=[UnicornClan],
    keywords=[Cavalry, Unique, Experienced("1"), Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Move home your target Personality."
Shinjo_Zhitae = Personality(
    card_id=12191,
    title="Shinjo Zhi-tae",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Commander, Samurai, SoulOf("Shinjo Ji-tae")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Give a target enemy Follower or Personality a Force penalty equal to Kazue's Personal Honor. Gain 1 Honor."
Utaku_Kazue = Personality(
    card_id=12192,
    title="Utaku Kazue",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
