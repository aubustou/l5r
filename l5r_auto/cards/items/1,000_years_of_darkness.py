from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Sword, TwoHanded, Weapon
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle/Open:</b> Destroy this Item. Give a target Ashalan Blade +3F/+3C.'
Ashalan_Blade = Item(card_id=601, title='Ashalan Blade', force=2, chi=2, gold_cost=5, focus_value=3, keywords=[Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])