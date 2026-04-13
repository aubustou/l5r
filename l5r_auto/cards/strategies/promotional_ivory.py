from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow your target unbowed Personality. Bow a target enemy Personality with lower Force. You may target and destroy one of his attachments if your Personality has <b>a</b> Weapon.'
Bisentodo = Strategy(card_id=10765, title='Bisento-do', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Gain 1 Honor.'
Colonial_Edict = Strategy(card_id=10766, title='Colonial Edict', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Open:</b> Bow your target unbowed Personality. Ranged 2 Attack targeting a card in a unit in another player's home, with +2 strength if your Personality is a Scout, and which bows its target instead of destroying it."
Scout_Tactics = Strategy(card_id=10599, title='Scout Tactics', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])