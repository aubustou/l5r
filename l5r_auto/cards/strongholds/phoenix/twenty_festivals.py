from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Temple
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Dynasty, :g*::</b> Recruit your target dead <i>(not discarded)</i> Phoenix Clan Personality; you may Proclaim him. Gain 1 Honor.<br><i>(When going second, you get +1PS and Personalities you Proclaim enter play for two less Gold.)</i>"
The_Majestic_Temple_of_the_Phoenix = Stronghold(
    card_id=12261,
    title="The Majestic Temple of the Phoenix",
    gold_production="4",
    starting_family_honor=6,
    province_strength=6,
    clan=[PhoenixClan],
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
