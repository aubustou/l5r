from __future__ import annotations
from .common import Spell
from l5r_auto.legality import DiamondEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Water Battle:</b> You may bow this Shugenja. If he bowed or if he is Water, negate other players' effects that move units to or from this battlefield. Destroy this Spell."
Summon_Water_Kami = Spell(card_id=7637, title='Summon Water Kami', gold_cost=3, focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, DiamondEdition, ModernEdition])