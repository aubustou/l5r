from __future__ import annotations

from l5r_auto.keywords import Farm, Retainer
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold. <br><b>Open:</b> If it is not your turn, target a Personality. Straighten his unit. Destroy this Holding."
Ashigaru_Fort = Holding(
    card_id=614,
    title="Ashigaru Fort",
    gold_cost=2,
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"<b>Interrupt, :bow::</b> If the action is another player's, before it destroys one of your Personalities at the current battlefield, create a 0F/1C/1PH Personality and transfer your first Personality's Followers to him. Destroy this Holding."
Reserve_Commander = Holding(
    card_id=6267,
    title="Reserve Commander",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
    gold_production="2",
)
