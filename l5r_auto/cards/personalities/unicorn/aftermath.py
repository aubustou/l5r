from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Commander,
    Destined,
    Reserve,
    Samurai,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Moto_Paikao = Personality(
    id=10887,
    title="Moto Paikao",
    force=3,
    chi=3,
    honor_requirement=3,
    personal_honor=2,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Commander, Samurai],
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
Utaku_Sakiko = Personality(
    id=10890,
    title="Utaku Sakiko",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=8,
    clan=[UnicornClan],
    keywords=[Cavalry, Destined, Reserve, BattleMaiden, Samurai],
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
