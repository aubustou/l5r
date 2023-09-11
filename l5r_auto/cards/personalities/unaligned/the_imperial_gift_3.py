from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Duelist, Ronin, Samurai
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Battle:</b> Give each Ronin Follower and Ronin Personality in Seasoned Ronin's army +1F."
Seasoned_Ronin = Personality(
    card_id=6532,
    title="Seasoned Ronin",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=1,
    clan=[Unaligned],
    keywords=[Ronin, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i>"
Tarui = Personality(
    card_id=7821,
    title="Tarui",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Duelist, Ronin, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
