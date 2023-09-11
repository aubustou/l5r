from __future__ import annotations

from l5r_auto.legality import (
    JadeEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"<b>Open:</b> Give each Nonhuman Personality +1F/+1C and give each Nonhuman Follower +1F."
Return_of_Myth = Event(
    card_id=6292,
    title="Return of Myth",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, JadeEdition, OnyxEdition, ModernEdition],
)
