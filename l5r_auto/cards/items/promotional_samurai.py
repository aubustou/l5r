from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Bow, TwoHanded, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Battle, :bow::</b> Ranged 2 Attack. You may destroy this Item to move this Personality home.'
Tsuruchi_Longbow = Item(card_id=8854, title='Tsuruchi Longbow', force=0, chi=0, gold_cost=3, focus_value=2, keywords=[Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])