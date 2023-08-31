from __future__ import annotations

from l5r_auto.keywords import Castle, Temple
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Temple_Fortress = Holding(
    card_id=7869,
    title="Temple Fortress",
    gold_cost=4,
    keywords=[Castle, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
Temple_to_the_Elements = Holding(
    card_id=7897,
    title="Temple to the Elements",
    gold_cost=6,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
