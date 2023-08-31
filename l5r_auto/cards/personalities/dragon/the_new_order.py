from __future__ import annotations

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

from ..common import Personality

Mirumoto_Touya = Personality(
    id=11897,
    title="Mirumoto Touya",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Mirumoto_Tsukino = Personality(
    id=11901,
    title="Mirumoto Tsukino",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=3,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Destined, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Mirumoto_Yoritama = Personality(
    id=11896,
    title="Mirumoto Yoritama",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Tamori_Chikyu = Personality(
    id=11898,
    title="Tamori Chikyu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Courtier, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Tamori_Daiishu = Personality(
    id=11899,
    title="Tamori Daiishu",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=2,
    clan=[DragonClan],
    keywords=[Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Togashi_Gozato_the_Wise_Monk = Personality(
    id=11900,
    title="Togashi Gozato, the Wise Monk",
    force=3,
    chi=5,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[LoveLetter, Monk, Samurai, Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
