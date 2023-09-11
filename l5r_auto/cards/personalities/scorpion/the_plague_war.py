from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import Courtier, Goryo, Nonhuman, Samurai, Shugenja
from l5r_auto.legality import (
    CelestialEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Tireless Interrupt:</b> If the action is yours and Political, straighten Orikasa after it resolves."
Shosuro_Orikasa = Personality(
    card_id=7149,
    title="Shosuro Orikasa",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
Shosuro_Rokujo = Personality(
    card_id=7155,
    title="Shosuro Rokujo",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Goryo, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        ModernEdition,
        ModernEdition,
    ],
)
