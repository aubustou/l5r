from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    ClanChampion,
    Commander,
    Conqueror,
    Duelist,
    Experienced,
    Kensai,
    Naval,
    Samurai,
    Thunder,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Yoritomo can only be controlled by his owner and has +1F/+1C for each of his Weapons. Followers and other Mantis Clan Personalities in Yoritomo's army have +1F while opposing a Shadowlands card.<br><b>Battle, :</b> Draw a card. Discard a card unless you <i>(now)</i> have fewer cards in your hand or fewer Provinces than any other player."
Yoritomo_Son_of_Storms_ExperiencedCW = Personality(
    card_id=12645,
    title="Yoritomo, Son of Storms",
    force=5,
    chi=4,
    personal_honor=3,
    gold_cost=14,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[
        Conqueror,
        Duelist,
        Kensai,
        Naval,
        Unique,
        ClanChampion,
        Commander,
        Experienced("1"),
        Samurai,
        Thunder,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
