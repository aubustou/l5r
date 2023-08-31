from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, SpiderClan
from l5r_auto.keywords import Kensai, Monk, OrderOfVenom
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

Suikotsu = Personality(
    id=7617,
    title="Suikotsu",
    force=4,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk, OrderOfVenom],
    traits=[],
    abilities=[],
    legality=[
        SamuraiEdition,
        CelestialEdition,
        ModernEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
    ],
)
