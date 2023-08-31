from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Port
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

The_Fruitful_Port_of_the_Mantis = Stronghold(
    card_id=11299,
    title="The Fruitful Port of the Mantis",
    gold_production="4",
    starting_family_honor=2,
    province_strength=7,
    clan=[MantisClan],
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
