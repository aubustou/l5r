from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import Courtier, Goryo, Nonhuman, Samurai, Shugenja
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Shosuro_Orikasa = Personality(
    id=7149,
    title="Shosuro Orikasa",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=7,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, ModernEdition, OnyxEdition],
)
Shosuro_Rokujo = Personality(
    id=7155,
    title="Shosuro Rokujo",
    force=2,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=4,
    clan=[ScorpionClan],
    keywords=[Courtier, Goryo, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, CelestialEdition, ModernEdition],
)
