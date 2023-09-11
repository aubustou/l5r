from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Duelist, Samurai
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Duelists win tied duels versus non-Duelists.)</i><br>After Izumiko wins a duel, gain 1 Honor."
Kakita_Izumiko = Personality(
    card_id=10576,
    title="Kakita Izumiko",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
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
