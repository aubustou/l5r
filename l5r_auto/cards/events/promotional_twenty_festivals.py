from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Event

Victory_of_the_Thunders = Event(
    card_id=12586,
    title="Victory of the Thunders",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
