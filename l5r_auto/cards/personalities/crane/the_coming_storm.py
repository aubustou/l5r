from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Braggart,
    Courtier,
    Destined,
    Duelist,
    Imperial,
    Jester,
    Magistrate,
    Reserve,
    Samurai,
    Scout,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

Daidoji_Ryushi = Personality(
    id=11734,
    title="Daidoji Ryushi",
    force=2,
    chi=1,
    honor_requirement=2,
    personal_honor=2,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Sutebo = Personality(
    id=11735,
    title="Daidoji Sutebo",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=7,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Natsuyo = Personality(
    id=11736,
    title="Doji Natsuyo",
    force=1,
    chi=3,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Burei = Personality(
    id=11737,
    title="Kakita Burei",
    force=2,
    chi=3,
    honor_requirement=5,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Duelist, Artisan, Braggart, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Jikeru = Personality(
    id=11738,
    title="Kakita Jikeru",
    force=0,
    chi=2,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Mitohime = Personality(
    id=11739,
    title="Kakita Mitohime",
    force=3,
    chi=3,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Destined, Duelist, Imperial, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
