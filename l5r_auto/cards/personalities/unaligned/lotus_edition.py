from __future__ import annotations

from l5r_auto.clans import RatlingFaction, Unaligned
from l5r_auto.keywords import Nonhuman, Ratling
from l5r_auto.legality import (
    DiamondEdition,
    LotusEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After Ratling Raider enters play, create two 2F/2C/2PH <b>Nonhuman &#149; Ratling</b> Personalities <i>(at his location)</i>."
Ratling_Raider = Personality(
    card_id=6175,
    title="Ratling Raider",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=None,
    clan=[Unaligned, RatlingFaction],
    keywords=[Nonhuman, Ratling],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
