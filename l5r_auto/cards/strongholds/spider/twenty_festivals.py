from __future__ import annotations

from l5r_auto.clans import SpiderClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

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
