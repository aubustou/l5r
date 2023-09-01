from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

The_Shadowed_Estate_of_the_Scorpion = Stronghold(
    card_id=11303,
    gold_production="4",
    starting_family_honor=1,
    province_strength=7,
    title="The Shadowed Estate of the Scorpion",
    clan=[ScorpionClan],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
