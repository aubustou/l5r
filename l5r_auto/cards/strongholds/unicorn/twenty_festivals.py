from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

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
