from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Spirit
from l5r_auto.legality import DiamondEdition, IvoryEdition, LotusEdition, ModernEdition, TwentyFestivalsEdition
'This Personality cannot attack unless he is a Shugenja. <br><b>Battle:</b> Fear 2, or Fear 4 if the target is a Follower.'
Souls_of_the_Fallen = Follower(card_id=7388, title='Souls of the Fallen', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Spirit], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, DiamondEdition, ModernEdition])