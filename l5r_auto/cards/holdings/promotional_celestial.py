from __future__ import annotations

from l5r_auto.keywords import Castle, Dojo, Port, SakeHouse
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Heavy_Infantry_Dojo = Holding(
    card_id=3044,
    title="Heavy Infantry Dojo",
    gold_cost=4,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Humble_House = Holding(
    card_id=3510,
    title="Humble House",
    gold_cost=2,
    keywords=[SakeHouse],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Merchant_Atoll = Holding(
    card_id=5027,
    title="Merchant Atoll",
    gold_cost=6,
    keywords=[Castle, Port],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
