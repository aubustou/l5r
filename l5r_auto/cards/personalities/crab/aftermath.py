from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    Destined,
    Hero,
    Imperial,
    Reserve,
    Samurai,
    Siege,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Hida_Kurabi = Personality(
    id=10832,
    title="Hida Kurabi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Destined, Reserve, Berserker, Hero, Imperial],
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
Kaiu_Gorobei = Personality(
    id=10835,
    title="Kaiu Gorobei",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
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
