from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Political Open, :bow::</b> If you control a Personality, gain 2 Honor.<br><i>(When going second, you get +1PS and a +5 Lobby bonus)</i>"
The_Esteemed_Palace_of_the_Crane = Stronghold(
    card_id=12258,
    title="The Esteemed Palace of the Crane",
    gold_production="4",
    starting_family_honor=6,
    province_strength=6,
    clan=[CraneClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
