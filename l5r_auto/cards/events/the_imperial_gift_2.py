from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Military_Alliance = Event(
    card_id=5054,
    title="Military Alliance",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
