from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    DiamondEdition,
    ImperialEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Doom_of_the_Dark_Lord = Event(
    card_id=2191,
    title="Doom of the Dark Lord",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[ImperialEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition],
)
Shadow_of_the_Dark_God = Event(
    card_id=6658,
    title="Shadow of the Dark God",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[ImperialEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition],
)
