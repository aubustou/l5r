from __future__ import annotations

from l5r_auto.keywords import Farm
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Miryoku_no_Shima = Holding(
    card_id=10268,
    title="Miryoku no Shima",
    gold_cost=6,
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
Vast_Paddy_Fields = Holding(
    card_id=10271,
    title="Vast Paddy Fields",
    gold_cost=2,
    keywords=[Farm],
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
