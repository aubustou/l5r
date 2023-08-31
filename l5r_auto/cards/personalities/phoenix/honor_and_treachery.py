from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Earth, Shugenja, SoulOf
from l5r_auto.legality import (
    EmperorEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Isawa_Nairuko = Personality(
    id=10242,
    title="Isawa Nairuko",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Earth, Shugenja, SoulOf("Isawa Mariko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, EmperorEdition, ModernEdition],
)
