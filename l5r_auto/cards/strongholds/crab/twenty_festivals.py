from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Battle:</b> Straighten your target opposed Personality. Straighten his attachments if your army has fewer units than the opposing army.<br><i>(When going second, you get +2PS and your Stronghold ability gains Tireless)</i>"
The_Unassailable_Fortress_of_the_Crab = Stronghold(
    card_id=12257,
    title="The Unassailable Fortress of the Crab",
    gold_production="4",
    starting_family_honor=3,
    province_strength=7,
    clan=[CrabClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
