from __future__ import annotations

from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Into_the_Wastes = Event(
    card_id=10820,
    title="Into the Wastes",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
