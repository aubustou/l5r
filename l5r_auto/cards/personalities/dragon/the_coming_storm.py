from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    BlessedByBenten,
    Cavalry,
    Courtier,
    Earth,
    Kensai,
    Magistrate,
    Monk,
    Samurai,
    Shugenja,
    Tattooed,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Kitsuki_Kira = Personality(
    id=11740,
    title="Kitsuki Kira",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Mirumoto_Reiji = Personality(
    id=11741,
    title="Mirumoto Reiji",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Cavalry, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Mirumoto_Takanori = Personality(
    id=11742,
    title="Mirumoto Takanori",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tamori_Junya = Personality(
    id=11743,
    title="Tamori Junya",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tamori_Touya = Personality(
    id=11744,
    title="Tamori Touya",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[BlessedByBenten, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Togashi_Yayoi = Personality(
    id=11745,
    title="Togashi Yayoi",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=2,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
