from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Courtier, Imperial
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Otomo_Demiyah = Personality(
    id=5812,
    title="Otomo Demiyah",
    force=2,
    chi=3,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=4,
    clan=[Unaligned],
    keywords=[Courtier, Imperial],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
