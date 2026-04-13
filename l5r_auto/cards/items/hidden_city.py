from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Bow, TwoHanded, Weapon
from l5r_auto.legality import DiamondEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'May only attach to a Samurai.<br><b>Battle, :bow::</b> Give a target enemy Follower or Personality -3F. You may then make a Ranged 0 Attack against that card if it is a legal target.'
Ichiros_Yumi = Item(card_id=3559, title="Ichiro's Yumi", force=0, chi=0, gold_cost=3, focus_value=2, keywords=[Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, DiamondEdition, ModernEdition])