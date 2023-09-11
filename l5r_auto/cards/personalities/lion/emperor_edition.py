from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import Samurai, Scout, Shugenja, Water
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Ikoma_Shika = Personality(
    card_id=3636,
    title="Ikoma Shika",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Samurai, Scout],
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
"<b>Limited:</b> Each player who controls an Ancestor gains 1 Honor. For any player who controls no Ancestors and has higher Honor than his starting Family Honor, you may choose to have him lose 1 Honor."
Kitsu_Suki = Personality(
    card_id=4396,
    title="Kitsu Suki",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Shugenja, Water],
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
