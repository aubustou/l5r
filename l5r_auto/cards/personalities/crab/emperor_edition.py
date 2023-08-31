from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Courtier, Merchant
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Yasuki_Tono = Personality(
    id=9467,
    title="Yasuki Tono",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=2,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
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
