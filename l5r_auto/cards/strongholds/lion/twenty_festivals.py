from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Battle:</b> Give your target opposed Samurai a Force bonus equal to his Personal Honor.<br><i>(When going second, you get +2PS and your Stronghold ability gains Tireless)</i>"
The_Grand_Halls_of_the_Lion = Stronghold(
    card_id=12260,
    title="The Grand Halls of the Lion",
    gold_production="3",
    starting_family_honor=7,
    province_strength=7,
    clan=[LionClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
