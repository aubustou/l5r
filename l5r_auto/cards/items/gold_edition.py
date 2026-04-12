from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Polearm, TwoHanded, Weapon
from l5r_auto.legality import GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, TwentyFestivalsEdition
Naginata = Item(card_id=5495, title='Naginata', force=1, chi=2, gold_cost=2, focus_value=1, keywords=[Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])