from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NagaFaction
from l5r_auto.keywords import Bushi, Naga, Nonhuman
from l5r_auto.legality import (
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Shabura = Personality(
    id=6645,
    title="Shabura",
    force=4,
    chi=2,
    honor_requirement=0,
    personal_honor=1,
    gold_cost=8,
    clan=[NagaFaction, NagaFaction],
    keywords=[Bushi, Naga, Nonhuman],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        IvoryEdition,
        JadeEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
    ],
)
