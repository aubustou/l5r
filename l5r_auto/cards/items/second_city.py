from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Tessen, Unique, Weapon
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Reaction:</b> When a Battle action would target a card in this unit, bow this card: The action targets another of your cards instead, if legal.'
Blade_of_Champions = Item(card_id=1004, title='Blade of Champions', force=3, chi=1, gold_cost=5, focus_value=3, keywords=[Unique, Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After a Ranged Attack from an action performed by this Personality targets a card without an attached Armor, bow this card: Give the Ranged Attack +2 strength.'
Flesh_Cutter_Arrows = Item(card_id=2608, title='Flesh Cutter Arrows', force=2, chi=0, gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Even if this card is bowed: Straighten this Personality or move him home.'
Fubatsu_Plate = Item(card_id=2719, title='Fubatsu Plate', force=4, chi=0, gold_cost=6, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target an enemy card: Bow it. Destroy it if it is an attachment and this Personality is Dragon Clan or a Kensai.'
Nightingale_Blade = Item(card_id=5556, title='Nightingale Blade', force=3, chi=1, gold_cost=4, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Enters play paying 1 less Gold if you are a Lion Clan player.<br><b>Reaction:</b> After this card enters play from your hand: Draw a card.'
Satoshis_Dual_Warfans = Item(card_id=6481, title="Satoshi's Dual Warfans", force=2, chi=1, gold_cost=3, focus_value=2, keywords=[Weapon, Tessen], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])