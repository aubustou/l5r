from __future__ import annotations

from l5r_auto.keywords import Dojo, Retainer
from l5r_auto.legality import (
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>Open, :bow::</b> Target your Monk or Shugenja Personality. After the next time <i>(this turn)</i> you announce an action on his Spell or your Kiho targets him, give him +2C until that action ends."
Blessed_Dojo = Holding(
    card_id=1027,
    title="Blessed Dojo",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
"<b>:bow::</b> Produce 1 Gold. <br><b>Open, :bow::</b> Transfer your target Follower from one of your unbowed Personalities to another."
Hida_Advisor = Holding(
    card_id=3067,
    title="Hida Advisor",
    gold_cost=1,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        GoldEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"This Holding has +2GP when it pays for a single Shugenja only."
Mystic_Dojo = Holding(
    card_id=5470,
    title="Mystic Dojo",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition],
)
