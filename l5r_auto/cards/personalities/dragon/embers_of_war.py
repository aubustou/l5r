from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import DragonClan
from l5r_auto.keywords import Cavalry, Earth, Mountaineer, Shugenja
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Tamori_Seiken = Personality(
    id=7790,
    title="Tamori Seiken",
    force=2,
    chi=3,
    honor_requirement=8,
    personal_honor=3,
    gold_cost=4,
    clan=[DragonClan],
    keywords=[Cavalry, Earth, Mountaineer, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, EmperorEdition, IvoryEdition, TwentyFestivalsEdition],
)
