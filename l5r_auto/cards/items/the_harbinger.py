from __future__ import annotations
from .common import Item
from l5r_auto.keywords import OneHanded, Sword, Thunder, Weapon
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'As a Focus Effect, after this duel ends, if your Personality won it, you may attach this Item to him, ignoring costs.'
Sadamune_Blade = Item(card_id=6443, title='Sadamune Blade', force=2, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])
'<b>Thunder Battle:</b> Move this Personality home. Straighten his unit as he moves.'
StormForged_Blade = Item(card_id=7510, title='Storm-Forged Blade', force=2, chi=0, gold_cost=2, focus_value=3, keywords=[Weapon, OneHanded, Sword, Thunder], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])