from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Commander,
    Courtier,
    Duelist,
    Earth,
    Expendable,
    Experienced,
    Fire,
    Kensai,
    Magistrate,
    Monk,
    Resilient,
    Samurai,
    Shugenja,
    Tactician,
    Tattooed,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Draw a card after your Expendable card dies.)</i><br>Compassion, or if you are Unicorn Clan: Akito has +2F/+2C. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Kitsuki_Akito = Personality(
    card_id=12296,
    title="Kitsuki Akito",
    force=1,
    chi=1,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Expendable, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack, or Ranged 4 Attack if the target is dishonorable."
Kitsuki_Mizukabe = Personality(
    card_id=12297,
    title="Kitsuki Mizukabe",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[DragonClan],
    keywords=[Resilient, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Straighten your target Ring. You may bow one of Higaru's Swords to straighten him."
Mirumoto_Higaru_Experienced = Personality(
    card_id=12298,
    title="Mirumoto Higaru",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Duelist, Kensai, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Battle:</b> Melee Attack equal to the number of Hirakura's Spirit Followers <i>(this is a Melee 0 Attack if he has no Spirit Followers)</i>."
Tamori_Hirakura = Personality(
    card_id=12299,
    title="Tamori Hirakura",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[DragonClan],
    keywords=[Resilient, Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Courtesy: Mabasu and his Spirit Followers have <b>Cavalry</b>. <i>(Courtesy traits do not take effect if you went first.)</i>"
Tamori_Mabasu = Personality(
    card_id=12300,
    title="Tamori Mabasu",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=3,
    clan=[DragonClan],
    keywords=[Tactician, Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Tameko enters play, give her three +1F Fire tokens.<br><b>Fire Battle:</b> Ranged Attack equal to the number of Tameko's Fire tokens, plus 1 if the target is Mantis Clan. Remove one of Tameko's Fire tokens."
Togashi_Tameko = Personality(
    card_id=12301,
    title="Togashi Tameko",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=4,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Fire, Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
