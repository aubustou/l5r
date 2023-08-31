from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Event

Alliance = Event(
    card_id=331,
    title="Alliance",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
    ],
)
Glimpse_of_the_Unicorn = Event(
    card_id=2818,
    title="Glimpse of the Unicorn",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
        ModernEdition,
    ],
)
