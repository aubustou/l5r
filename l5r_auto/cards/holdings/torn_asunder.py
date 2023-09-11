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

"<b>Open:</b> Target two of your Personalities. A lesson is taught. One copies Commander, Duelist, Kensai, Magistrate, Paragon, Scout, or Yojimbo from the other."
Miryoku_no_Shima = Holding(
    card_id=10268,
    title="Miryoku no Shima",
    gold_cost=6,
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
    gold_production="5",
)
"<b>:bow::</b> Produce 2 Gold. If you bowed this Holding while paying to Recruit a Farm Holding, refill the Province face-up."
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
    gold_production="2",
)
