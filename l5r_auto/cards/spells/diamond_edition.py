from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Fire
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Fire Battle:</b> Bow this Shugenja to make a Ranged 2 Attack. <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force.)</i><br><b>Air Battle:</b> Move this Shugenja to an adjacent, unresolved battlefield or move him home.'
Fire_and_Air = Spell(card_id=2557, title='Fire and Air', gold_cost=2, focus_value=2, keywords=[Air, Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])