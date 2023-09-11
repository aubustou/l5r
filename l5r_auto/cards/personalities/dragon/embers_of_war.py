from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.keywords import Cavalry, Earth, Mountaineer, Shugenja
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i><i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle. Shugenja may attach and cast Spells.)</i></i>"
Tamori_Seiken = Personality(
    card_id=7790,
    title="Tamori Seiken",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=8,
    clan=[DragonClan],
    keywords=[Cavalry, Earth, Mountaineer, Shugenja],
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
