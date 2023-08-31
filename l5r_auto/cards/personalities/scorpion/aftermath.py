from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import Magistrate, Samurai
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Bayushi_Mifuyu = Personality(
    id=10869,
    title="Bayushi Mifuyu",
    force=4,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[ScorpionClan],
    keywords=[Magistrate, Samurai],
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
