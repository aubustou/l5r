from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.keywords import Alchemist, Earth, Shugenja
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i><br><b>Earth Battle:</b> Bow a target enemy card without attachments."
Tamori_Jinai = Personality(
    card_id=10633,
    title="Tamori Jinai",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Alchemist, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
