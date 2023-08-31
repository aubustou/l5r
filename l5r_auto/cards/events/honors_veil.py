from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

A_Prophet_Revealed = Event(
    card_id=66,
    title="A Prophet Revealed",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[SamuraiEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
