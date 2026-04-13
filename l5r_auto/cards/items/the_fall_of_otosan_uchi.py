from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Sword, TwoHanded, Weapon
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'This Item has +2C while this Personality is dueling a Personality with lower Force.'
Dotanuki = Item(card_id=2202, title='Dotanuki', force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])