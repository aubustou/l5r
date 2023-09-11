from __future__ import annotations

from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"<b>Engage:</b> You have the first opportunity in this battle to pass or take a Battle action, which must come from a card in a unit."
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
