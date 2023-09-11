from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Stronghold

"<i>(This card has +1PS and +2GP if you didn't go first.)</i><br><b>Limited, :g4::</b> Gain 2 Honor. <br><b>Tireless Battle:</b> Discard a card to make a Fear effect with strength equal to the card's Focus Value. <i>(Tireless actions may be taken even while bowed.)</i>"
Gates_of_the_Second_City = Stronghold(
    card_id=11142,
    title="Gates of the Second City",
    gold_production="8",
    starting_family_honor=8,
    province_strength=7,
    clan=[Unaligned],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
