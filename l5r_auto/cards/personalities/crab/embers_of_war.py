from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Courtier, Kolat, Merchant, Samurai, Scholar, Scout
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Hiruma_Moritoki = Personality(
    id=3307,
    title="Hiruma Moritoki",
    force=4,
    chi=3,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=6,
    clan=[CrabClan],
    keywords=[Samurai, Scholar, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
Yasuki_Makoto = Personality(
    id=9449,
    title="Yasuki Makoto",
    force=2,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[CrabClan],
    keywords=[Courtier, Kolat, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
