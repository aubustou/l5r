from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import (
    Courtier,
    Empress,
    Experienced,
    Imperial,
    Loyal,
    Seductress,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot gain Corruption tokens or Shadowlands.<br><b>Dynasty/Open, :bow::</b> Kachiko may remain bowed. Target a Personality. While Kachiko remains bowed, after each time the target assigns, the target's controller's turn begins, and your turn begins if the target is Shadowlands, give the target a -1F/-1C Poison token. Remove these tokens if Kachiko straightens or leaves play."
Bayushi_Kachiko_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12647,
    title="Bayushi Kachiko, Seven Thunder",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[
        Experienced("2CW"),
        Loyal,
        Unique,
        Courtier,
        Empress,
        Imperial,
        Seductress,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
