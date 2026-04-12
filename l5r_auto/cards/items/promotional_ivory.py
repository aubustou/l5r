from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Polearm, TwoHanded, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle:</b> Give a target enemy Personality or Follower -3F.'
Deadly_Bisento = Item(card_id=10763, title='Deadly Bisento', force=3, chi=2, gold_cost=8, focus_value=4, keywords=[Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])