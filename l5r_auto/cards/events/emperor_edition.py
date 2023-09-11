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

"<b>Open:</b> Starting with you, each player may search his discard pile and Fate deck for a Ring, show it, and put it in his hand."
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
