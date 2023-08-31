from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    ClanChampion,
    Commander,
    Experienced,
    Hero,
    Jade,
    Loyal,
    Resilient,
    Samurai,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Hida_Yakamo_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12640,
    title="Hida Yakamo, Seven Thunder",
    force=6,
    chi=4,
    personal_honor=4,
    gold_cost=14,
    honor_requirement=6,
    clan=[CrabClan],
    keywords=[
        Experienced("2CW"),
        Loyal,
        Resilient,
        Tactician,
        Unique,
        ClanChampion,
        Commander,
        Hero,
        Jade,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
