from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Duelist,
    Merchant,
    Resilient,
    Samurai,
    Scout,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Daidoji_Hirota = Personality(
    card_id=11568,
    title="Daidoji Hirota",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Daidoji_Natsuki = Personality(
    card_id=11569,
    title="Daidoji Natsuki",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Daidoji_Takeda = Personality(
    card_id=11570,
    title="Daidoji Takeda",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kakita_Ariyoshi = Personality(
    card_id=11571,
    title="Kakita Ariyoshi",
    force=1,
    chi=5,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Artisan, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kakita_Mariko = Personality(
    card_id=11572,
    title="Kakita Mariko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=0,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kakita_Shinichi = Personality(
    card_id=11573,
    title="Kakita Shinichi",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Duelist, Resilient, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
