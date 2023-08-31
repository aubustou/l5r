from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Paragon, Samurai
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

Matsu_Misato = Personality(
    id=4956,
    title="Matsu Misato",
    force=3,
    chi=3,
    honor_requirement=10,
    personal_honor=3,
    gold_cost=6,
    clan=[LionClan],
    keywords=[Paragon, Samurai],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        SamuraiEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
    ],
)
