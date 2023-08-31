from __future__ import annotations

from l5r_auto.keywords import Port
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Fortified_Docks = Holding(
    card_id=2666,
    title="Fortified Docks",
    gold_cost=2,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
