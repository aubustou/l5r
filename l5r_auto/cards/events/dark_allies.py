from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"Each player may take only one Limited or Open action per turn <i>(after this Event enters play)</i>.<br><b>Open:</b> If you have not taken an action this phase, put this Event into play. Discard it after the current active player's next Action Phase begins."
Short_Season = Event(
    card_id=7082,
    title="Short Season",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
