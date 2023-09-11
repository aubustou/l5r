from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Courtier, Kolat, Merchant, Samurai, Scholar, Scout
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Hiruma_Moritoki = Personality(
    card_id=3307,
    title="Hiruma Moritoki",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai, Scholar, Scout],
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
"Your Holdings enter play for 1 less Gold. <br><b>Economic Home Battle, :bow::</b> Target an enemy Personality. His controller may pay 4 Gold. If he does, he loses 1 Honor. If he does not, dishonor the target and move him home."
Yasuki_Makoto = Personality(
    card_id=9449,
    title="Yasuki Makoto",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Courtier, Kolat, Merchant],
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
