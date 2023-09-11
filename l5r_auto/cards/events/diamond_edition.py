from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    DiamondEdition,
    ImperialEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"Each player draws an additional card at the end of his turn. After each time a player must draw a card but cannot because his deck is empty, destroy his rightmost Province.<br><b>Open:</b> Put this Event into play."
Doom_of_the_Dark_Lord = Event(
    card_id=2191,
    title="Doom of the Dark Lord",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[ImperialEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition],
)
"Provinces have -1 strength.<br><b>Open:</b> Put this Event into play."
Shadow_of_the_Dark_God = Event(
    card_id=6658,
    title="Shadow of the Dark God",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[ImperialEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition],
)
