from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<i>(A Personality can only have one Armor.)</i> <br>After the first time each turn another player's Battle action targets this Personality, that player may discard a card; if he does not, negate the action."
Eternal_Armor = Item(card_id=2385, title='Eternal Armor', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Armor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])