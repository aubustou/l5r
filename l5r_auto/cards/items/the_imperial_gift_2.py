from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Knife, OneHanded, Sword, Weapon
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(A Personality can only have one Weapon.)</i>'
A_Samurais_Soul = Item(card_id=76, title="A Samurai's Soul", force=2, chi=1, gold_cost=2, focus_value=2, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])
"<i>(A Personality can only have one Weapon.)</i><br><b>Battle:</b> Ranged Attack equal to this Personality's Force. Destroy this Item."
Throwing_Knives = Item(card_id=8463, title='Throwing Knives', force=1, chi=0, gold_cost=3, focus_value=1, keywords=[Weapon, Knife, OneHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])