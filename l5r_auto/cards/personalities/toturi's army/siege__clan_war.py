from __future__ import annotations

from l5r_auto.clans import ToturisArmy, Unaligned
from l5r_auto.keywords import (
    Commander,
    Duelist,
    Experienced,
    Ronin,
    Samurai,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot gain Corruption tokens or Shadowlands. Can only be controlled by his owner. Lion Clan players may Proclaim Toturi. Other players' Fear effects targeting cards in Toturi's army have -1 strength.<br><b>Tireless Battle:</b> Toturi unites the Lion Clan. Another target Personality's printed abilities may be used an additional time this turn. Straighten them or take an additional action."
Toturi_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12644,
    title="Toturi, Seven Thunder",
    force=6,
    chi=5,
    personal_honor=5,
    gold_cost=15,
    honor_requirement=10,
    clan=[ToturisArmy, Unaligned],
    keywords=[
        Duelist,
        Experienced("2CW"),
        Tactician,
        Unique,
        Commander,
        Ronin,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
