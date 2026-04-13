from __future__ import annotations
from .common import Item
from l5r_auto.keywords import OneHanded, Tessen, Weapon
from l5r_auto.legality import CelestialEdition, IvoryEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'After this Item leaves play, remove it from the game. <br>You may Equip this Item from your discard pile as a <b>Battle</b> action.'
GumbaiUchiwa = Item(card_id=2922, title='Gumbai-Uchiwa', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Weapon, OneHanded, Tessen], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, CelestialEdition, SamuraiEdition, ModernEdition])