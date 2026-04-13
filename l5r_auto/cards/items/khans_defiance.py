from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor
from l5r_auto.legality import LotusEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'Ranged Attacks targeting cards in this unit have -2 strength.<br><b>Tireless Battle:</b> Move this Personality home. <i>(Tireless actions may be taken even while bowed.)</i>'
Lacquered_Armor = Item(card_id=4656, title='Lacquered Armor', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Armor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, OnyxEdition, SamuraiEdition, ModernEdition])