from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    Destined,
    Hero,
    Imperial,
    Reserve,
    Samurai,
    Siege,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Draw a card after you Recruit a Destined card. You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i>"
Hida_Kurabi = Personality(
    card_id=10832,
    title="Hida Kurabi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Destined, Reserve, Berserker, Hero, Imperial],
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
"<b>Battle:</b> Discard a card to bow a target enemy card with Force equal to or lower than the discarded card's Focus Value."
Kaiu_Gorobei = Personality(
    card_id=10835,
    title="Kaiu Gorobei",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
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
