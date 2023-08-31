from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Duelist, Kenku, Nonhuman
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Shune = Personality(
    id=7236,
    title="Shune",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Duelist, Kenku, Nonhuman],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
