from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Commander,
    Destined,
    Reserve,
    Samurai,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Battle:</b> Discard a card to give a target enemy Follower or Personality a Force penalty equal to the card's Focus Value."
Moto_Paikao = Personality(
    card_id=10887,
    title="Moto Paikao",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle. Draw a card after you Recruit a Destined card. You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i>"
Utaku_Sakiko = Personality(
    card_id=10890,
    title="Utaku Sakiko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Destined, Reserve, BattleMaiden, Samurai],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
