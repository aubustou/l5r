from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Air,
    Artisan,
    Courtier,
    Cursed,
    Daimyo,
    Duelist,
    Expendable,
    Experienced,
    IronCrane,
    Jester,
    Loyal,
    Magistrate,
    Poet,
    Reserve,
    Samurai,
    Shugenja,
    SoulOf,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i><br><b>Open:</b> Target another player's Personality. After the next time this turn he is destroyed during a battle, gain 2 Honor."
Asahina_Hirakane = Personality(
    card_id=12091,
    title="Asahina Hirakane",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Air, Shugenja, SoulOf("Asahina Minori")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Hiroteru has +1F for each bowed card in the enemy army.<br><b>Battle:</b> Fear 3."
Daidoji_Hiroteru = Personality(
    card_id=12092,
    title="Daidoji Hiroteru",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[IronCrane, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Taenaru is destroyed, gain 2 Honor.<br><b>Battle:</b> Once per battle, move home a target enemy Personality with lower current Force than his own printed Force. Bow him as he moves."
Daidoji_Taenaru = Personality(
    card_id=12093,
    title="Daidoji Taenaru",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Samurai, SoulOf("Daidoji Tae")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br><b>Interrupt:</b> After Masachika enters play, dishonor a target Personality with equal or lower Personal Honor."
Doji_Masachika = Personality(
    card_id=12094,
    title="Doji Masachika",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=7,
    clan=[CraneClan],
    keywords=[Expendable, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Absent Home Battle:</b> Move Norime into your defending army. After this moves her, you may target and bow an enemy dishonorable Personality. <i>(Absent actions may be taken without presence. Home actions may be taken from home.)</i>"
Doji_Norime = Personality(
    card_id=12095,
    title="Doji Norime",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Engage:</b> If Senkiku opposes a dishonorable Personality, gain 2 Honor."
Doji_Senkiku = Personality(
    card_id=12096,
    title="Doji Senkiku",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai, SoulOf("Doji Hitomaro")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Interrupt:</b> Before another player loses Honor from the action, Tashihime's poems immortalize the shame; increase the loss by 1 and gain 1 Honor."
Doji_Tashihime = Personality(
    card_id=12097,
    title="Doji Tashihime",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=8,
    clan=[CraneClan],
    keywords=[Artisan, Poet, SoulOf("Doji Nukada")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Interrupt, :bow::</b> If the action is yours, before you gain Honor from it, negate the gain to make a target player lose 1 Honor."
Kakita_Akitomo = Personality(
    card_id=12098,
    title="Kakita Akitomo",
    force=0,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br>After you Proclaim Hikai or he is destroyed, a target player loses 1 Honor."
Kakita_Hikai = Personality(
    card_id=12099,
    title="Kakita Hikai",
    force=0,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Expendable, Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Ikura will not attack or issue challenges, and cannot be challenged from Iaijutsu actions.<br><b>Favor Political Open:</b> Discard the Imperial Favor to make a target player lose 1 Honor."
Kakita_Ikura = Personality(
    card_id=12100,
    title="Kakita Ikura",
    force=1,
    chi=5,
    personal_honor=3,
    gold_cost=9,
    honor_requirement=8,
    clan=[CraneClan],
    keywords=[Loyal, Unique, Artisan, Courtier, Cursed, Daimyo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i> <br>Mitsumichi will not refuse challenges. If Mitsumichi is honorable, the first card another player focuses in each duel against him is focused face-up."
Kakita_Mitsumichi = Personality(
    card_id=12101,
    title="Kakita Mitsumichi",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Samurai, SoulOf("Kakita Yariga")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Ujirou enters play, you may take an additional action. While you are the Defender, you Recruit Ujirou for 5 less Gold.<br><b>Battle:</b> Fear 4 that destroys attachments and dishonorable Personalities after it bows them."
Kakita_Ujirou_Experienced = Personality(
    card_id=12102,
    title="Kakita Ujirou",
    force=4,
    chi=4,
    personal_honor=3,
    gold_cost=11,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Duelist, Reserve, Unique, Experienced("1"), Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
