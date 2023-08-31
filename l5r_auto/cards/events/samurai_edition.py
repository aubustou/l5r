from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    ImperialEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Enlistment = Event(
    card_id=2346,
    title="Enlistment",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        ImperialEdition,
        OnyxEdition,
        SamuraiEdition,
        ModernEdition,
    ],
)
Severed_from_the_Emperor = Event(
    card_id=6636,
    title="Severed from the Emperor",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        ImperialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
