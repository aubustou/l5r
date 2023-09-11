from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Commander,
    Destined,
    Experienced,
    Magistrate,
    Reserve,
    Samurai,
    Scout,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i><br><b>Battle, :bow::</b> Ranged 2 Attack. Straighten Baatar if he has a Spear, the Ranged Attack targeted a Phoenix Clan Personality, or he entered play this battle."
Moto_Baatar = Personality(
    card_id=12337,
    title="Moto Baatar",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Chairei has +1F if you are Dragon Clan.<br>Courtesy: Chairei has Cavalry. <i>(Courtesy traits do not take effect if you went first.)</i>"
Shinjo_Chairei = Personality(
    card_id=12338,
    title="Shinjo Chairei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i><br><b>Battle:</b> Give a target enemy Personality a Force penalty equal to your target unbowed Personality's Personal Honor."
Shinjo_Tsungmin = Personality(
    card_id=12339,
    title="Shinjo Tsung-min",
    force=3,
    chi=1,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br>Masako has +1F/+1C for each of your Provinces that have been destroyed this game."
Utaku_Masako = Personality(
    card_id=12340,
    title="Utaku Masako",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Melee 3 Attack that may bow the target instead of destroying it; if this bows the target, gain 2 Honor. If Sakiko has entered play or moved this turn, straighten her."
Utaku_Sakiko_Experienced = Personality(
    card_id=12341,
    title="Utaku Sakiko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=5,
    clan=[UnicornClan],
    keywords=[
        Cavalry,
        Destined,
        Reserve,
        BattleMaiden,
        Experienced("1"),
        Magistrate,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'Compassion: Zo Sia has the ability, "<b>Open, :</b> If Zo Sia is honorably dead, put her face-up in your target Province, discarding any card there." <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>'
Utaku_Zo_Sia = Personality(
    card_id=12342,
    title="Utaku Zo Sia",
    force=1,
    chi=2,
    personal_honor=4,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
