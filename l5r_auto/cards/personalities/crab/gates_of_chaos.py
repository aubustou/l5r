from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Destined, Samurai, Scout
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Draw a card after you Recruit a Destined card.)</i><br><b>Battle, :bow::</b> Ranged 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>."
Toritaka_Iabuchi = Personality(
    card_id=10621,
    title="Toritaka Iabuchi",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Destined, Samurai, Scout],
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
