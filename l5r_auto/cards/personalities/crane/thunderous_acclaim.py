from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Duelist,
    Expendable,
    Experienced,
    IronCrane,
    Magistrate,
    Poet,
    Resilient,
    Samurai,
    Spy,
    Storyteller,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Kuraou has +1F/+1C while he has a Spear or opposes a Crab Clan Personality.<br><b>Battle:</b> Give a target enemy Personality -3F."
Daidoji_Kuraou = Personality(
    card_id=12290,
    title="Daidoji Kuraou",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=1,
    clan=[CraneClan],
    keywords=[IronCrane, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: Buredo has +1F/+1C/+1PH. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i><br>Phoenix Clan players may Proclaim Buredo."
Doji_Buredo = Personality(
    card_id=12291,
    title="Doji Buredo",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=None,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: Hoshihana has Destined. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i><br><b>Tireless Open:</b> If you have resolved an action from a Political Strategy this turn, straighten Hoshihana."
Doji_Hoshihana = Personality(
    card_id=12292,
    title="Doji Hoshihana",
    force=1,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Poet, Storyteller],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i> <br><b>Iaijutsu Battle:</b> Fear 2. If this bowed a Personality with lower Personal Honor, give Moro +1F."
Doji_Moro = Personality(
    card_id=12293,
    title="Doji Moro",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Open:</b> Target another player's Personality. After the first time <i>(this turn)</i> the target assigns or moves to a battlefield, move Iwari there, and if the target is attacking, his player loses 1 Honor, or 2 Honor if the target is Crab Clan."
Kakita_Iwari = Personality(
    card_id=12294,
    title="Kakita Iwari",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[CraneClan],
    keywords=[Expendable, Artisan, Courtier, Spy],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Shinichi's focused cards have +1FV while you control, or he is dueling, Kakita Daitsu.<br><b>Iaijutsu Unstoppable Battle:</b> Shinichi challenges a target enemy Personality, who may move home to refuse. Bow the loser."
Kakita_Shinichi_Experienced = Personality(
    card_id=12295,
    title="Kakita Shinichi",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=9,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Resilient, Experienced("1"), Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
