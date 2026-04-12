from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Guard, Imperial
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle, :bow::</b> Ranged 2 Attack. <br><b>Battle:</b> Fear 2.'
Incendiary_Archers = Follower(card_id=11308, title='Incendiary Archers', force=2, chi=0, gold_cost=4, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Negate Fear effects targeting this Follower. This Follower has +2F while you control the Imperial Favor. If this Personality ever attacks, destroy this Follower.'
Iweko_Honor_Guard = Follower(card_id=11246, title='Iweko Honor Guard', force=4, chi=0, gold_cost=7, focus_value=3, keywords=[Guard, Imperial], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Ranged 2 Attack.'
Spearmen_Cavalry = Follower(card_id=11309, title='Spearmen Cavalry', force=2, chi=0, gold_cost=4, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])