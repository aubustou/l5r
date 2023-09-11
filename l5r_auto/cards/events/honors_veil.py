from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"After your action resolves, if any targets of its Ranged Attacks are still in play, straighten any of your cards that the action and combining abilities bowed.<br><b>Open:</b> Put this Event into play."
A_Prophet_Revealed = Event(
    card_id=66,
    title="A Prophet Revealed",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[SamuraiEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
