from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Ningyo, Nonhuman, Scout, StormRider
from l5r_auto.legality import (
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

Sasada = Personality(
    id=6476,
    title="Sasada",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=4,
    clan=[MantisClan],
    keywords=[Naval, Ningyo, Nonhuman, Scout, StormRider],
    traits=[],
    abilities=[],
    legality=[
        SamuraiEdition,
        ModernEdition,
        IvoryEdition,
        LotusEdition,
        TwentyFestivalsEdition,
    ],
)
