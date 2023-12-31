from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Cavalry,
    Commander,
    Conqueror,
    Duelist,
    Experienced,
    Loyal,
    Samurai,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot gain Corruption tokens or Shadowlands. Kamoko's Followers must be Cavalry. After Kamoko enters play, create and attach to her a 1F Cavalry Follower with the trait, \"After Kamoko's Battle action targets Yogo Junzo, destroy him.\" <br><b>Battle:</b> If they would be opposed, move a target Personality at any location to the current battlefield. If Kamoko is attacking, you may target and destroy a card without attachments in the Personality's unit."
Otaku_Kamoko_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12649,
    title="Otaku Kamoko, Seven Thunder",
    force=5,
    chi=4,
    personal_honor=3,
    gold_cost=16,
    honor_requirement=8,
    clan=[UnicornClan],
    keywords=[
        Cavalry,
        Conqueror,
        Duelist,
        Experienced("2CW"),
        Loyal,
        Unique,
        Commander,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
