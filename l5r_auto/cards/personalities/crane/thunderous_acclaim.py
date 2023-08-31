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
