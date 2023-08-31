from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Asako_Misora = Personality(
    id=10861,
    title="Asako Misora",
    force=1,
    chi=4,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[PhoenixClan],
    keywords=[Expendable, Earth, Inquisitor, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[
        OnyxEdition,
        ModernEdition,
        IvoryEdition,
        EmperorEdition,
        TwentyFestivalsEdition,
    ],
)
Isawa_Ikariya = Personality(
    id=10862,
    title="Isawa Ikariya",
    force=4,
    chi=4,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=9,
    clan=[PhoenixClan],
    keywords=[Reserve, Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[
        OnyxEdition,
        ModernEdition,
        IvoryEdition,
        EmperorEdition,
        TwentyFestivalsEdition,
    ],
)
