from __future__ import annotations
from .common import Item
from l5r_auto.keywords import OneHanded, Sword, Weapon
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<i>(A Personality can only have one Weapon.)</i>'
Fubatsu_Blade = Item(card_id=2717, title='Fubatsu Blade', force=3, chi=1, gold_cost=4, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, SamuraiEdition, ModernEdition])