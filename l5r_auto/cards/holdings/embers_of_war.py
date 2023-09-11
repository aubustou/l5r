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

"After the first time each turn you bow this Holding, gain 1 Honor."
Temple_Fortress = Holding(
    card_id=7869,
    title="Temple Fortress",
    gold_cost=4,
    keywords=[Castle, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 5 Gold. <br><b>Open:</b> Give your target Monk or Shugenja <b>Air</b>, <b>Earth</b>, <b>Fire</b>, or <b>Water</b>."
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
    gold_production="5",
)
