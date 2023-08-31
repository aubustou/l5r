from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Cavalry, Samurai
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Hida_Iguchi = Personality(
    id=10575,
    title="Hida Iguchi",
    force=3,
    chi=1,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=4,
    clan=[CrabClan],
    keywords=[Cavalry, Samurai],
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
