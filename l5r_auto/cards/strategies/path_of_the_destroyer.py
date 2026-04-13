from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle:</b> Target your opposed Personality: Give him +3F.<br><b>Battle:</b> Target an enemy Follower or Item: Destroy it.'
Crushing_Strength = Strategy(card_id=1589, title='Crushing Strength', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Open:</b> Target another player's Human Personality. His controller may have him commit seppuku <i>(rehonor, then destroy him)</i>. If he chose this, he gains 4 Honor. If he did not choose this, dishonor the Personality, and his controller loses 2 Honor."
Test_of_Sincerity = Strategy(card_id=7931, title='Test of Sincerity', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])