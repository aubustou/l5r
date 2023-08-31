from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Destined,
    Duelist,
    Fire,
    LoveLetter,
    Naval,
    Nonhuman,
    Orochi,
    Samurai,
    ScionOfFlame,
    ScionOfTheSea,
    Shugenja,
    Water,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Isawa_Fujigawa = Personality(
    id=11916,
    title="Isawa Fujigawa",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Isawa_Nomura = Personality(
    id=11914,
    title="Isawa Nomura",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Fire, ScionOfFlame, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Isawa_Tenkawa_the_Scholar = Personality(
    id=11915,
    title="Isawa Tenkawa, the Scholar",
    force=0,
    chi=5,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Air, LoveLetter, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kyuji = Personality(
    id=11917,
    title="Kyuji",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=9,
    clan=[PhoenixClan],
    keywords=[Cavalry, Naval, Nonhuman, Orochi, ScionOfTheSea, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shiba_Kintaro_the_Remembered = Personality(
    id=11919,
    title="Shiba Kintaro, the Remembered",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Destined, Duelist, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shiba_Koshiba = Personality(
    id=11918,
    title="Shiba Koshiba",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=1,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
