from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Cavalry,
    Commander,
    Conqueror,
    Duelist,
    Experienced,
    Loyal,
    Samurai,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Otaku_Kamoko_Seven_Thunder_Experienced_2CW = Personality(
    id=12649,
    title="Otaku Kamoko, Seven Thunder",
    force=5,
    chi=4,
    honor_requirement=8,
    personal_honor=3,
    gold_cost=16,
    clan=[UnicornClan],
    keywords=[
        Cavalry,
        Conqueror,
        Duelist,
        Experienced("2CW"),
        Loyal,
        Unique,
        Commander,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
