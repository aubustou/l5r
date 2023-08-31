from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import BitterLies, Conqueror, Samurai
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Bayushi_Aibako = Personality(
    card_id=10581,
    title="Bayushi Aibako",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Conqueror, BitterLies, Samurai],
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
