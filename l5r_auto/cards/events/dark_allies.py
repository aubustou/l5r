from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Short_Season = Event(
    card_id=7082,
    title="Short Season",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
