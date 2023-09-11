from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<b>Tireless Open:</b> Name a Fate card, or name a Dynasty card in play. Negate the effects of the next action from a card with that title.<br><i>(When going second, you get +1PS and other players have -1 maximum hand size)</i>"
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
