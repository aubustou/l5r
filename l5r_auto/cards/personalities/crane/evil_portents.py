from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Duelist,
    Expendable,
    Experienced,
    Jester,
    Kensai,
    Magistrate,
    Resilient,
    Samurai,
    TheMaskedCrane,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Doji_Ikei = Personality(
    card_id=12446,
    title="Doji Ikei",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Doji_Natsuyo_Experienced = Personality(
    card_id=12447,
    title="Doji Natsuyo",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=8,
    clan=[CraneClan],
    keywords=[Courtier, Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Doji_Soeka_Experienced = Personality(
    card_id=12448,
    title="Doji Soeka",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, Experienced("1"), Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kakita_Daitsu_Experienced = Personality(
    card_id=12449,
    title="Kakita Daitsu",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Kensai, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kakita_Inaka = Personality(
    card_id=12450,
    title="Kakita Inaka",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kakita_Oshaberi = Personality(
    card_id=12451,
    title="Kakita Oshaberi",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Expendable, Artisan, Courtier, TheMaskedCrane],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
