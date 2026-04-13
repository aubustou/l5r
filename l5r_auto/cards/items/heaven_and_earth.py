from __future__ import annotations
from .common import Item
from l5r_auto.keywords import OneHanded, Sword, Weapon
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'After you Equip this Item, gain 1 Honor. <br>Before this Personality is dishonored, destroy this Item and negate the dishonoring.'
Blessed_Sword = Item(card_id=1029, title='Blessed Sword', force=1, chi=1, gold_cost=2, focus_value=2, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])