from __future__ import annotations

from l5r_auto.clans import ToturisArmy, Unaligned
from l5r_auto.keywords import (
    Commander,
    Duelist,
    Experienced,
    Ronin,
    Samurai,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Toturi_Seven_Thunder_Experienced_2CW = Personality(
    id=12644,
    title="Toturi, Seven Thunder",
    force=6,
    chi=5,
    personal_honor=5,
    gold_cost=15,
    honor_requirement=10,
    clan=[ToturisArmy, Unaligned],
    keywords=[
        Duelist,
        Experienced("2CW"),
        Tactician,
        Unique,
        Commander,
        Ronin,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
