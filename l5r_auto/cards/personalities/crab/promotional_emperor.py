from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Cavalry, Samurai
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i>"
Hida_Iguchi = Personality(
    card_id=10575,
    title="Hida Iguchi",
    force=3,
    chi=1,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Cavalry, Samurai],
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
