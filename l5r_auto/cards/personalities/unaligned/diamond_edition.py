from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import (
    Fire,
    Nonhuman,
    Ogre,
    Oni,
    Samurai,
    Shadowlands,
    SoulOf,
    Undead,
)
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Fushiki_no_Oni = Personality(
    id=2749,
    title="Fushiki no Oni",
    force=5,
    chi=4,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=8,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Fire, Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, DiamondEdition, TwentyFestivalsEdition],
)
Gekido_no_Oni = Personality(
    id=2786,
    title="Gekido no Oni",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=6,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        JadeEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
        DiamondEdition,
    ],
)
Ogre_Bushi = Personality(
    id=5675,
    title="Ogre Bushi",
    force=6,
    chi=4,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=9,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Ogre, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        ModernEdition,
        GoldEdition,
        JadeEdition,
        ImperialEdition,
        IvoryEdition,
        TwentyFestivalsEdition,
        DiamondEdition,
    ],
)
Voitagi = Personality(
    id=9182,
    title="Voitagi",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=3,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Samurai, Shadowlands, SoulOf("Uragirimono"), Undead],
    traits=[],
    abilities=[],
    legality=[
        OnyxEdition,
        ModernEdition,
        GoldEdition,
        TwentyFestivalsEdition,
        DiamondEdition,
    ],
)
