from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Destined,
    Duelist,
    Expendable,
    Fire,
    Kensai,
    Magistrate,
    Monk,
    Samurai,
    Shadowlands,
    Shugenja,
    Smith,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Daigotsu_Takahide = Personality(
    id=11926,
    title="Daigotsu Takahide",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Gyushi_Kageto = Personality(
    id=11927,
    title="Gyushi Kageto",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Artisan, Fire, Shugenja, Smith],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Kokujin_Dairu_Student_of_the_Dark_Lotus = Personality(
    id=11928,
    title="Kokujin Dairu, Student of the Dark Lotus",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[Destined, Kensai, Monk, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Kokujin_Kuchika_Blood_of_the_Dark_Lotus = Personality(
    id=11929,
    title="Kokujin Kuchika, Blood of the Dark Lotus",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[Kensai, Monk, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Susumu_Issei = Personality(
    id=11930,
    title="Susumu Issei",
    force=0,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Susumu_Kengo = Personality(
    id=11931,
    title="Susumu Kengo",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Expendable, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
