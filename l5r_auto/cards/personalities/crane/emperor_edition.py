from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Commander, IronCrane, Samurai, Scout, SoulOf
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Battle:</b> Give a target enemy Follower or Personality -4F. You may target your Personality and move him home."
Daidoji_Tametaka = Personality(
    card_id=1682,
    title="Daidoji Tametaka",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Commander, IronCrane, Samurai, Scout, SoulOf("Daidoji Zoushi")],
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
