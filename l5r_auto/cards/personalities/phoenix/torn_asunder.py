from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Fire, Shugenja
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i><br><b>Fire Battle/Open:</b> Give Hibana -3F. Give your target non-Water Personality +3F."
Isawa_Hibana = Personality(
    card_id=10305,
    title="Isawa Hibana",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Fire, Shugenja],
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
