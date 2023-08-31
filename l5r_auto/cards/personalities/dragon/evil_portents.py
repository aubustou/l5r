from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Commander,
    Courtier,
    Destined,
    Duelist,
    Earth,
    Experienced,
    Magistrate,
    Monk,
    Resilient,
    Samurai,
    Shugenja,
    Tattooed,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Kitsuki_Goshi = Personality(
    id=12452,
    title="Kitsuki Goshi",
    force=3,
    chi=3,
    honor_requirement=5,
    personal_honor=3,
    gold_cost=7,
    clan=[DragonClan],
    keywords=[Destined, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kitsuki_Goto = Personality(
    id=12453,
    title="Kitsuki Goto",
    force=0,
    chi=3,
    honor_requirement=5,
    personal_honor=3,
    gold_cost=4,
    clan=[DragonClan],
    keywords=[Resilient, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Mirumoto_Konoe = Personality(
    id=12454,
    title="Mirumoto Konoe",
    force=3,
    chi=3,
    honor_requirement=3,
    personal_honor=1,
    gold_cost=5,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Sannin = Personality(
    id=12455,
    title="Sannin",
    force=3,
    chi=3,
    honor_requirement=3,
    personal_honor=1,
    gold_cost=6,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Tamori_Daiishu_Experienced = Personality(
    id=12456,
    title="Tamori Daiishu",
    force=3,
    chi=4,
    honor_requirement=2,
    personal_honor=2,
    gold_cost=8,
    clan=[DragonClan],
    keywords=[Commander, Earth, Experienced("1"), Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Tamori_Gaitsuru = Personality(
    id=12457,
    title="Tamori Gaitsuru",
    force=2,
    chi=3,
    honor_requirement=2,
    personal_honor=1,
    gold_cost=5,
    clan=[DragonClan],
    keywords=[Destined, Resilient, Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
