from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Reserve, Samurai, Scout, Thunder
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

Tsuruchi_Gosho = Personality(
    id=8833,
    title="Tsuruchi Gosho",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[MantisClan],
    keywords=[Naval, Reserve, Samurai, Scout, Thunder],
    traits=[],
    abilities=[],
    legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition, CelestialEdition],
)
