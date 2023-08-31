from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Ronin, Shugenja, Void
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Enomoto = Personality(
    id=2348,
    title="Enomoto",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[Unaligned],
    keywords=[Ronin, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition, CelestialEdition],
)
