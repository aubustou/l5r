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

"After Fushiki enters play, lose 4 Honor.<br><b>Fire Battle:</b> Destroy a target Fortification at this battlefield with Gold Cost lower than Fushiki's Force. Give Fushiki a +1F token."
Fushiki_no_Oni = Personality(
    card_id=2749,
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
    legality=[TwentyFestivalsEdition, OnyxEdition, DiamondEdition, ModernEdition],
)
"After you Recruit Gekido, lose 3 Honor. Cannot attach Followers or Items. <br><b>Battle/Open:</b> Give Gekido +2F/+3C until this phase ends. After the phase ends, give Gekido -2F/-2C until your next turn ends."
Gekido_no_Oni = Personality(
    card_id=2786,
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
        TwentyFestivalsEdition,
        JadeEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"Cannot attach Armor or Followers."
Ogre_Bushi = Personality(
    card_id=5675,
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
        TwentyFestivalsEdition,
        ImperialEdition,
        GoldEdition,
        JadeEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"After Voitagi enters play, lose 3 Honor.<br><b>Battle:</b> Fear 3 <i>(Bow a target enemy Follower or Personality without Followers with 3 or lower Force)</i>."
Voitagi = Personality(
    card_id=9182,
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
        TwentyFestivalsEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
