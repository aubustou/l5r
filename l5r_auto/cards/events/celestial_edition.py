from __future__ import annotations

from l5r_auto.keywords import Festival, Unique
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

A_New_Year = Event(
    card_id=59,
    title="A New Year",
    keywords=[Festival],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
A_Time_for_Action = Event(
    card_id=89,
    title="A Time for Action",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        GoldEdition,
        ModernEdition,
    ],
)
Claiming_the_Throne = Event(
    card_id=1400,
    title="Claiming the Throne",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        OnyxEdition,
        TwentyFestivalsEdition,
    ],
)
The_New_Order = Event(
    card_id=8235,
    title="The New Order",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        CelestialEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
