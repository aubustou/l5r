from __future__ import annotations

from l5r_auto.keywords import Retainer
from l5r_auto.legality import (
    DiamondEdition,
    GoldEdition,
    LotusEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"This Holding has +1GP, but only when it pays for a single non-Shadowlands Naga or Human Personality without your Clan Alignment; gain 1 Honor after he enters play."
Honored_Sensei = Holding(
    card_id=3440,
    title="Honored Sensei",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
"<b>Political Open, :bow::</b> If the active player has 11 or more Family Honor, he loses 1 Honor."
Puppet_Theater_Troupe = Holding(
    card_id=6101,
    title="Puppet Theater Troupe",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
