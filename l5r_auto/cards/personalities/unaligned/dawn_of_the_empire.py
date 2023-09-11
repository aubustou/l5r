from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Nonhuman, Oni, Shadowlands
from l5r_auto.legality import (
    DiamondEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After you Recruit Hatsu Suru, lose 5 Honor.<br>After another player's card destroys Hatsu Suru, remove it from the game, lose 4 Honor, and create two 2F/2C/0PH <b>Nonhuman &#149; Oni &#149; Shadowlands</b> Personalities at Hatsu Suru's former location."
Hatsu_Suru_no_Oni = Personality(
    card_id=5734,
    title="Hatsu Suru no Oni",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
