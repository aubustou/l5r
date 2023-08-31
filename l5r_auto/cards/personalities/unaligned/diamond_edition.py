from __future__ import annotations

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

from ..common import Personality

Fushiki_no_Oni = Personality(
    id=2749,
    title="Fushiki no Oni",
    force=5,
    chi=4,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Fire, Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[DiamondEdition, TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Gekido_no_Oni = Personality(
    id=2786,
    title="Gekido no Oni",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        DiamondEdition,
        TwentyFestivalsEdition,
        JadeEdition,
        ModernEdition,
    ],
)
Ogre_Bushi = Personality(
    id=5675,
    title="Ogre Bushi",
    force=6,
    chi=4,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Ogre, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        ImperialEdition,
        DiamondEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
    ],
)
Voitagi = Personality(
    id=9182,
    title="Voitagi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Samurai, Shadowlands, SoulOf("Uragirimono"), Undead],
    traits=[],
    abilities=[],
    legality=[
        OnyxEdition,
        DiamondEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
    ],
)
