from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Earth,
    ElementalMaster,
    Experienced,
    Jade,
    Loyal,
    Magistrate,
    Resilient,
    Shugenja,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Isawa_Tadaka_Seven_Thunder_Experienced_2CW = Personality(
    id=12646,
    title="Isawa Tadaka, Seven Thunder",
    force=4,
    chi=5,
    personal_honor=3,
    gold_cost=12,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[
        Experienced("2CW"),
        Loyal,
        Resilient,
        Unique,
        Earth,
        ElementalMaster,
        Jade,
        Magistrate,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
