from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Ningyo, Nonhuman, Scout, StormRider
from l5r_auto.legality import (
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br><b>Tireless Battle/Open:</b> Bow your target unbowed Port. Straighten Sasada."
Sasada = Personality(
    card_id=6476,
    title="Sasada",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Ningyo, Nonhuman, Scout, StormRider],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
