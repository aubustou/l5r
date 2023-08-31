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
