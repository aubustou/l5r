from __future__ import annotations

from l5r_auto.keywords import Dojo
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Nexus_of_Lies = Holding(
    card_id=10827,
    title="Nexus of Lies",
    gold_cost=4,
    gold_production="4",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Suana_Dojo = Holding(
    card_id=10828,
    title="Suana Dojo",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Yukihimes_Hot_Springs = Holding(
    card_id=10830,
    title="Yukihime's Hot Springs",
    gold_cost=1,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
