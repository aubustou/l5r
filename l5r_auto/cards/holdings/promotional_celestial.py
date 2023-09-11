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

"<b>:bow::</b> Produce 3 Gold. <br><b>Battle, :bow::</b> Give your target Personality +2F."
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
"<b>:bow::</b> Produce 2 Gold. <br><b>Limited, :bow::</b> Give a target Personality a +1F <b>Sake </b>token. Remove it after your next turn begins."
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
"Your Provinces have +1 strength. <br><b>:bow::</b> Produce 5 Gold."
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
