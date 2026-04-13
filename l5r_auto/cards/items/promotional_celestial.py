from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Weapon
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'This card enters play bowed.<br>This Personality has +2 Gold Cost.<br><b>Reaction:</b> When a Holding bows to produce Gold, bow this card: The Holding produces one additional Gold.'
Coin_Pouch = Item(card_id=1427, title='Coin Pouch', force=0, chi=0, gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After an action targets this Personality, discard a card: Negate this Personality's movement from the action's effects."
Colonists_Mark = Item(card_id=1432, title="Colonist's Mark", force=0, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Ranged Attacks targeting this Personality have -2 strength.'
Inexpensive_Armor = Item(card_id=3742, title='Inexpensive Armor', force=0, chi=0, gold_cost=0, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card with lower Force than this Personality and no attachments: Destroy it.<br><b>Battle:</b> Move this Personality to the current battlefield if he assigned there.'
Wyrmbone_Katana = Item(card_id=9414, title='Wyrmbone Katana', force=4, chi=1, gold_cost=8, focus_value=4, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])