from __future__ import annotations

from l5r_auto.keywords import Dojo, Retainer
from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

Blessed_Dojo = Holding(
    card_id=1027,
    title="Blessed Dojo",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
Hida_Advisor = Holding(
    card_id=3067,
    title="Hida Advisor",
    gold_cost=1,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Mystic_Dojo = Holding(
    card_id=5470,
    title="Mystic Dojo",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
