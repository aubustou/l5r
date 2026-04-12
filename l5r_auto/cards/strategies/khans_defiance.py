from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import IvoryEdition, LotusEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
"<b>Battle:</b> Target your unbowed Samurai and target a Personality in the Defender's home. Straighten his unit. The Defender may move him to the current battlefield. If he chose not to, he loses 2 Honor, dishonor the Personality, and you may draw two cards."
Coward = Strategy(card_id=1544, title='Coward!', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, SamuraiEdition, ModernEdition])
"<b>Battle:</b> Target your unbowed Samurai or Berserker Personality. Bow one or two target enemy units with a total Gold Cost less than your Personality's unit's total Gold Cost. Destroy any cards in the enemy units with 0 Gold Cost."
Standing_Fast = Strategy(card_id=7467, title='Standing Fast', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, OnyxEdition, SamuraiEdition, ModernEdition])