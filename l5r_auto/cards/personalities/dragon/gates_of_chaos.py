from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import DragonClan
from l5r_auto.keywords import Alchemist, Earth, Shugenja
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Tamori_Jinai = Personality(
    id=10633,
    title="Tamori Jinai",
    force=3,
    chi=4,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=8,
    clan=[DragonClan],
    keywords=[Alchemist, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[
        OnyxEdition,
        ModernEdition,
        IvoryEdition,
        EmperorEdition,
        TwentyFestivalsEdition,
    ],
)
