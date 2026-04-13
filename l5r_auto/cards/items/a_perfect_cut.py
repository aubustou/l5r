from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Sword, TwoHanded, Weapon
from l5r_auto.legality import GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"Negate this Personality's Force and Chi bonuses <i>(Modifiers from Items are not bonuses)</i>."
Tachi = Item(card_id=7714, title='Tachi', force=3, chi=3, gold_cost=7, focus_value=1, keywords=[Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition])