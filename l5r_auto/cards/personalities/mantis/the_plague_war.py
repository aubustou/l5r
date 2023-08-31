from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Ningyo, Nonhuman, Shugenja, Thunder
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Sarassa = Personality(
    id=6475,
    title="Sarassa",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Ningyo, Nonhuman, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition, CelestialEdition],
)
