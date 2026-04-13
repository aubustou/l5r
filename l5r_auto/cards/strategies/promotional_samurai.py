from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import IvoryEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow your target unbowed Ring. Bow a target enemy card without attachments. <br><b>Battle:</b> Target your bowed Ring and an attachment. Straighten both targets.'
Aligned_with_the_Elements = Strategy(card_id=321, title='Aligned with the Elements', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])
'<b>Political Battle:</b> Destroy your target Courtier. Bow a target enemy Personality. Move him home. This movement will not be negated.'
Desperate_Sacrifice = Strategy(card_id=1977, title='Desperate Sacrifice', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
"<b>Open, :g2::</b> Bow your target unbowed Courtier or Ninja. Target another player's Personality. After the next time <i>(this turn)</i> his controller assigns him, targets him, or an action from a card in his unit resolves, give him two -1F/-1C Poison tokens."
Poison_Sake = Strategy(card_id=5994, title='Poison Sake', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])