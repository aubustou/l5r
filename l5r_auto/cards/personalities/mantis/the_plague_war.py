from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Ningyo, Nonhuman, Shugenja, Thunder
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Sarassa = Personality(
    id=6475,
    title="Sarassa",
    force=4,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=8,
    clan=[MantisClan],
    keywords=[Naval, Ningyo, Nonhuman, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, ModernEdition, OnyxEdition],
)
