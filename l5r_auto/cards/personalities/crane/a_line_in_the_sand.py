from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Daidoji_Hirota = Personality(
    id=11568,
    title="Daidoji Hirota",
    force=2,
    chi=3,
    honor_requirement=6,
    personal_honor=2,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
Daidoji_Natsuki = Personality(
    id=11569,
    title="Daidoji Natsuki",
    force=2,
    chi=2,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
Daidoji_Takeda = Personality(
    id=11570,
    title="Daidoji Takeda",
    force=3,
    chi=2,
    honor_requirement=2,
    personal_honor=1,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
Kakita_Ariyoshi = Personality(
    id=11571,
    title="Kakita Ariyoshi",
    force=1,
    chi=5,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=8,
    clan=[CraneClan],
    keywords=[Artisan, Courtier],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
Kakita_Mariko = Personality(
    id=11572,
    title="Kakita Mariko",
    force=3,
    chi=3,
    honor_requirement=0,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
Kakita_Shinichi = Personality(
    id=11573,
    title="Kakita Shinichi",
    force=2,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Duelist, Resilient, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition],
)
