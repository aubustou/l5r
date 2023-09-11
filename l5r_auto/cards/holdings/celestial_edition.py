from __future__ import annotations

from l5r_auto.keywords import Market
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"You may only have one copy of Counting House in play.<br><b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> If you have fewer Provinces than each other player, draw a card."
Counting_House = Holding(
    card_id=1528,
    title="Counting House",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"After you Recruit this Holding from a Province, refill the Province face-up.<br><b>:bow::</b> Produce 2 Gold."
Famous_Bazaar = Holding(
    card_id=2470,
    title="Famous Bazaar",
    gold_cost=2,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"<b>:bow::</b> Produce 4 Gold.<br><b>Tireless Interrupt, :gstar::</b> If this Holding bowed to produce Gold to Recruit a Personality, Equip an attachment to him from your hand for 4 less Gold after he enters play."
Secluded_Outpost = Holding(
    card_id=6535,
    title="Secluded Outpost",
    gold_cost=6,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="4",
)
