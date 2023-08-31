from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan, SpiritFaction
from l5r_auto.keywords import Courtier, Shugenja, Spirit
from l5r_auto.legality import (
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

Yogo_Honami = Personality(
    id=9491,
    title="Yogo Honami",
    force=2,
    chi=4,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=7,
    clan=[ScorpionClan, SpiritFaction, SpiritFaction],
    keywords=[Courtier, Shugenja, Spirit],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, SamuraiEdition],
)
