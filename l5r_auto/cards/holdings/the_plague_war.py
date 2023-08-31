from __future__ import annotations

from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

The_Blessed_Herd = Holding(
    card_id=7975,
    title="The Blessed Herd",
    gold_cost=7,
    gold_production="6",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
