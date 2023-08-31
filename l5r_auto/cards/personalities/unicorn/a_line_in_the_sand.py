from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Bully,
    Cavalry,
    Courtier,
    DeathPriest,
    Destined,
    Kensai,
    Merchant,
    Resilient,
    Samurai,
    Shugenja,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Ide_Ryou = Personality(
    id=11616,
    title="Ide Ryou",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Iuchi_Kalsang = Personality(
    id=11617,
    title="Iuchi Kalsang",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=2,
    clan=[UnicornClan],
    keywords=[Cavalry, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Moto_Alani = Personality(
    id=11618,
    title="Moto Alani",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Destined, Resilient, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Moto_KyouakuInu = Personality(
    id=11619,
    title="Moto Kyouaku-Inu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shinjo_Shimikoto = Personality(
    id=11620,
    title="Shinjo Shimikoto",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Resilient, Bully, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Utaku_Kimiono = Personality(
    id=11621,
    title="Utaku Kimiono",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
