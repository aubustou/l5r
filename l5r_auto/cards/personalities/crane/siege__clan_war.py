from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import ClanChampion, Duelist, Experienced, Loyal, Samurai, Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Doji_Hoturi_Seven_Thunder_Experienced_2CW = Personality(
    id=12641,
    title="Doji Hoturi, Seven Thunder",
    force=5,
    chi=6,
    honor_requirement=10,
    personal_honor=4,
    gold_cost=15,
    clan=[CraneClan],
    keywords=[Duelist, Experienced("2CW"), Loyal, Unique, ClanChampion, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
