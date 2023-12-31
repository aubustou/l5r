from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Reserve, Samurai, Scout, Thunder
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(You may Recruit a Reserve Personality, if he would be opposed, as an Absent Battle action.)</i> <br><b>Thunder Absent Interrupt:</b> After you Recruit Gosho at this battlefield, Ranged 3 Attack."
Tsuruchi_Gosho = Personality(
    card_id=8833,
    title="Tsuruchi Gosho",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Reserve, Samurai, Scout, Thunder],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
