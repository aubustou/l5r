from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Ninja, Shadowlands, Unique, Weapon
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'As a Focus Effect, after this duel ends, bow its winner.<br><b>Reaction, :gstar::</b> After one of your Personalities enters play, Equip this Item to him.'
A_Simple_Yari = Item(card_id=78, title='A Simple Yari', force=3, chi=0, gold_cost=3, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Fear Battle:</b> Target an enemy Follower: Bow it.'
Crimson_Shadow_Armor = Item(card_id=1564, title='Crimson Shadow Armor', force=3, chi=0, gold_cost=3, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"You must declare an attack each turn and assign this Personality to attack if possible.<br><b>Reaction:</b> After an action targets this Personality: Negate this Personality's movement from the action's effects."
Hunger = Item(card_id=3514, title='Hunger', force=5, chi=1, gold_cost=6, focus_value=4, keywords=[Unique, Weapon, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Attaches to a Courtier for 2 less Gold. <br><b>Political Limited:</b> Target a dishonorably dead Personality. His owner loses Honor equal to the Personality's printed Personal Honor. Remove this Item from the game."
Record_of_Failure = Item(card_id=6213, title='Record of Failure', force=0, chi=0, gold_cost=2, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'Will only attach to a Ninja.<br><b>Battle:</b> Choose your performing Ninja, and destroy this card or discard it from your hand: Ranged 3 Attack.'
Tsubute = Item(card_id=8772, title='Tsubute', force=1, chi=0, gold_cost=0, focus_value=2, keywords=[Weapon, Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])