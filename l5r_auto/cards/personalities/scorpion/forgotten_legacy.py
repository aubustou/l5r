from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import BitterLies, Kensai, Loyal, Paragon, Samurai, Yojimbo
from l5r_auto.legality import (
    CelestialEdition,
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br><b>Battle:</b> Bow a target enemy card without attachments. If Toshimo has a Weapon or you control a Courtier, the card cannot straighten."
Bayushi_Toshimo = Personality(
    card_id=916,
    title="Bayushi Toshimo",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, Loyal, BitterLies, Paragon, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
