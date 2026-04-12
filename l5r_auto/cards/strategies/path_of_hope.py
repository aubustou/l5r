from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import LotusEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Political Interrupt:</b> If the action is another player's, negate its effects that dishonor or give Shadowlands to your target Personality.<br><b>Political Battle/Open:</b> Give a target Personality -1F, or -3F if you control a Magistrate."
Unexpected_Testimony = Strategy(card_id=8979, title='Unexpected Testimony', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, OnyxEdition, ModernEdition])