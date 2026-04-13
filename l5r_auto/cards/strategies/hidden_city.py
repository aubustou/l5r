from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Terrain
from l5r_auto.legality import DiamondEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Personalities at this battlefield have a Force penalty equal to their Personal Honor. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Blind_Honor = Strategy(card_id=1043, title='Blind Honor', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, DiamondEdition, ModernEdition])