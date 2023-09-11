from __future__ import annotations

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

from ..common import Personality

Kitsune_Kohaki = Personality(
    card_id=4467,
    title="Kitsune Kohaki",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=2,
    clan=[MantisClan, SpiritFaction],
    keywords=[Earth, Kitsune, Nonhuman, Shugenja, Spirit],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit. Shugenja may attach and cast Spells.)</i><br><b>Thunder Battle:</b> Bow a target enemy card without attachments."
Moshi_Yokohime = Personality(
    card_id=5290,
    title="Moshi Yokohime",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Shugenja, SoulOf("Moshi Yuriko"), Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
