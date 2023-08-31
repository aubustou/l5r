from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

The_Fortified_Monastery_of_the_Dragon = Stronghold(
    card_id=12259,
    title="The Fortified Monastery of the Dragon",
    gold_production="4",
    starting_family_honor=5,
    province_strength=6,
    clan=[DragonClan],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition],
)
