from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import (
    Courtier,
    Empress,
    Experienced,
    Imperial,
    Loyal,
    Seductress,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Bayushi_Kachiko_Seven_Thunder_Experienced_2CW = Personality(
    id=12647,
    title="Bayushi Kachiko, Seven Thunder",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[
        Experienced("2CW"),
        Loyal,
        Unique,
        Courtier,
        Empress,
        Imperial,
        Seductress,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
