from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"This Stronghold produces 4 Gold on your first turn.<br><b>Battle/Engage:</b> If he would be opposed, move your target unbowed Personality in a Cavalry unit at any location to the current battlefield.<br><i>(When going second, you get +1PS and a second use of Cycle on any turn)</i>"
The_Endless_Plains_of_the_Unicorn = Stronghold(
    card_id=12263,
    title="The Endless Plains of the Unicorn",
    gold_production="5",
    starting_family_honor=4,
    province_strength=7,
    clan=[UnicornClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
