from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, SpiderClan
from l5r_auto.keywords import Kensai, Monk, OrderOfVenom
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Battle:</b> Bow a target enemy Personality with lower Force and without a Weapon."
Suikotsu = Personality(
    card_id=7617,
    title="Suikotsu",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk, OrderOfVenom],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
