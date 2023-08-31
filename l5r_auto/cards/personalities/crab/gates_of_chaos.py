from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Destined, Samurai, Scout
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Toritaka_Iabuchi = Personality(
    id=10621,
    title="Toritaka Iabuchi",
    force=3,
    chi=2,
    honor_requirement=3,
    personal_honor=2,
    gold_cost=7,
    clan=[CrabClan],
    keywords=[Destined, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
    ],
)
