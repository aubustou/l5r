from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Political
from l5r_auto.legality import IvoryEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Assassin Dark Virtue Battle:</b> Target your unbowed Samurai. Destroy a target enemy bowed card.'
Assassins_Strike = Strategy(card_id=626, title="Assassin's Strike", focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Bow two of your target unbowed Personalities and target an enemy Personality. Bow his unit.'
Pack_Tactics = Strategy(card_id=5859, title='Pack Tactics', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Give your target opposed Personality a Force bonus equal to his Personal Honor.'
Strength_of_my_Father = Strategy(card_id=7543, title='Strength of my Father', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])
'<b>Political Open:</b> Target another player who controls an attachment and destroy your target attachment. He may choose and destroy one of his attachments. If he did not choose this, gain Honor equal to the Focus Value of your destroyed attachment.'
Wary_Peace = Strategy(card_id=9239, title='Wary Peace', gold_cost=0, focus_value=4, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])