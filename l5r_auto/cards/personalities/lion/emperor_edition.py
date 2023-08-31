from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import Samurai, Scout, Shugenja, Water
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Ikoma_Shika = Personality(
    id=3636,
    title="Ikoma Shika",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Kitsu_Suki = Personality(
    id=4396,
    title="Kitsu Suki",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
