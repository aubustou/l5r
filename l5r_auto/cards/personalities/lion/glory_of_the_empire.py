from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import Paragon, Samurai
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Matsu_Misato = Personality(
    id=4956,
    title="Matsu Misato",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Paragon, Samurai],
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
)
