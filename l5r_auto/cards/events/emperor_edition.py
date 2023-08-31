from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    EmperorEdition,
    IvoryEdition,
    JadeEdition,
    LotusEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Wisdom_Gained = Event(
    card_id=9356,
    title="Wisdom Gained",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        CelestialEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
