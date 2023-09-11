from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Earth,
    Expendable,
    Fire,
    Inquisitor,
    Magistrate,
    Reserve,
    Shugenja,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Draw a card after your Expendable card dies. Shugenja may attach and cast Spells.)</i>"
Asako_Misora = Personality(
    card_id=10861,
    title="Asako Misora",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Expendable, Earth, Inquisitor, Magistrate, Shugenja],
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
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i><br><b>Fire Battle:</b> Ranged Attack equal to the number of Spells in this unit."
Isawa_Ikariya = Personality(
    card_id=10862,
    title="Isawa Ikariya",
    force=4,
    chi=4,
    personal_honor=2,
    gold_cost=9,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Reserve, Fire, Shugenja],
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
