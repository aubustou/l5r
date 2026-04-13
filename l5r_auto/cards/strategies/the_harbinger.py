from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"As a Focus Effect, this duel's winner gains 1 Honor after it ends.<br><b>Open:</b> If you have not played another Flashy Technique this turn, Personalities have -1F while attacking."
Flashy_Technique = Strategy(card_id=2602, title='Flashy Technique', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target your unbowed Samurai. Target an enemy Personality with lower Chi. Bow him or all his attachments.'
Pacify = Strategy(card_id=5858, title='Pacify', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])