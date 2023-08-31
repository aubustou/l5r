from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Samurai, Scout, Shugenja, Water
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Ikoma_Shika = Personality(
    id=3636,
    title="Ikoma Shika",
    force=2,
    chi=2,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=2,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
Kitsu_Suki = Personality(
    id=4396,
    title="Kitsu Suki",
    force=0,
    chi=4,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=6,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
