from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Courtier, Merchant
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Yasuki_Tono = Personality(
    id=9467,
    title="Yasuki Tono",
    force=0,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=2,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
