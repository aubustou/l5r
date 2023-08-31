from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import ClanChampion, Duelist, Experienced, Loyal, Samurai, Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Doji_Hoturi_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12641,
    title="Doji Hoturi, Seven Thunder",
    force=5,
    chi=6,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=10,
    clan=[CraneClan],
    keywords=[Duelist, Experienced("2CW"), Loyal, Unique, ClanChampion, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
