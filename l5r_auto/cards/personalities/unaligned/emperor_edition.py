from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Courtier, Imperial
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Otomo_Demiyah = Personality(
    card_id=5812,
    title="Otomo Demiyah",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Courtier, Imperial],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
