from __future__ import annotations

from l5r_auto.legality import (
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

The_Heavens_Are_Watching = Event(
    card_id=8123,
    title="The Heavens Are Watching",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition],
)
