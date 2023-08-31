from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Commander,
    Courtier,
    Destined,
    Duelist,
    Earth,
    Kensai,
    LoveLetter,
    Monk,
    Samurai,
    Shugenja,
    Tattooed,
    Void,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

Mirumoto_Touya = Personality(
    id=11897,
    title="Mirumoto Touya",
    force=3,
    chi=4,
    honor_requirement=7,
    personal_honor=3,
    gold_cost=7,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Mirumoto_Tsukino = Personality(
    id=11901,
    title="Mirumoto Tsukino",
    force=2,
    chi=2,
    honor_requirement=4,
    personal_honor=1,
    gold_cost=3,
    clan=[DragonClan],
    keywords=[Destined, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Mirumoto_Yoritama = Personality(
    id=11896,
    title="Mirumoto Yoritama",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=6,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Tamori_Chikyu = Personality(
    id=11898,
    title="Tamori Chikyu",
    force=2,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=6,
    clan=[DragonClan],
    keywords=[Courtier, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Tamori_Daiishu = Personality(
    id=11899,
    title="Tamori Daiishu",
    force=3,
    chi=4,
    honor_requirement=2,
    personal_honor=2,
    gold_cost=6,
    clan=[DragonClan],
    keywords=[Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Togashi_Gozato_the_Wise_Monk = Personality(
    id=11900,
    title="Togashi Gozato, the Wise Monk",
    force=3,
    chi=5,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=7,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[LoveLetter, Monk, Samurai, Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
