from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.legality import ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"After all players reveal Strongholds, search your Fate deck for a non-Void Ring, and put it into play; Sensei effects that remove abilities also remove this trait.<br><i>(When going second, you get +1PS, +1 maximum hand size, and begin with an extra card in your hand.)</i>"
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
