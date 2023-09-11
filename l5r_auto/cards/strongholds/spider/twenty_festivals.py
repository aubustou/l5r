from __future__ import annotations

from l5r_auto.clans import SpiderClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Tireless Battle:</b> Fear 3. <i>(Bow a target enemy Follower or Personality without Followers with 3 or lower Force)</i><br><i>(When going second, you have +1 Province Strength, your Fear has +1 strength, and you may, if any of your Provinces have been destroyed, refill the first Province during your Dynasty Phase face-up)</i>"
The_Hidden_Bastion_of_the_Spider = Stronghold(
    card_id=12262,
    title="The Hidden Bastion of the Spider",
    gold_production="4",
    starting_family_honor=0,
    province_strength=8,
    clan=[SpiderClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
