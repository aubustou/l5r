from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan, SpiritFaction
from l5r_auto.keywords import (
    Earth,
    Kitsune,
    Naval,
    Nonhuman,
    Shugenja,
    SoulOf,
    Spirit,
    Thunder,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Kitsune_Kohaki = Personality(
    id=4467,
    title="Kitsune Kohaki",
    force=3,
    chi=4,
    honor_requirement=2,
    personal_honor=3,
    gold_cost=6,
    clan=[MantisClan, SpiritFaction],
    keywords=[Earth, Kitsune, Nonhuman, Shugenja, Spirit],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
Moshi_Yokohime = Personality(
    id=5290,
    title="Moshi Yokohime",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[MantisClan],
    keywords=[Naval, Shugenja, SoulOf("Moshi Yuriko"), Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, EmperorEdition, OnyxEdition],
)
