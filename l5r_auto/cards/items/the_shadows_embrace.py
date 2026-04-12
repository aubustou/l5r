from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Experienced, Keitaku, Megumi, Unique, Weapon, Yuruginai
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Battle:</b> Remove this card from the game: Each player chooses zero to two Personalities at the current battlefield. Remove them from the game; cards and tokens stay attached to them. After the next turn begins, each unit enters play in its owner's home, ignoring costs, restrictions, and entering-play effects; then, give them each three +1F <b>Blood</b> tokens."
Blood_of_the_Preserver = Item(card_id=9875, title='Blood of the Preserver', force=0, chi=0, gold_cost=4, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Crab Clan Personality.<br>This card has +1F for each Crab Clan Personality you control. <br>After this card enters play: Gain 2 Honor.<br><b>Battle/Open:</b> Even if this card is bowed: Straighten this unit.'
Celestial_Sword_of_the_Crab_Experienced = Item(card_id=9876, title='Celestial Sword of the Crab', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), Yuruginai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only Equip to a Crane Clan Personality.<br>This Item has +1F for each Crane Clan Personality you control.<br>After this Item enters play, gain 2 Honor.<br><b>Favor Political Open:</b> Give a target Personality or Follower -4F. You may discard the Imperial Favor to gain 1 Honor.'
Celestial_Sword_of_the_Crane_Experienced = Item(card_id=9877, title='Celestial Sword of the Crane', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), Megumi], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Will only attach to a Phoenix Clan Personality.<br>This card has +1F for each Phoenix Clan Personality you control.<br>After this card enters play: Gain 2 Honor.<br><b>Battle/Open:</b> Target your honorably dead Phoenix Clan Personality: Bring him into play at this card's location, ignoring costs. Remove him from the game before the turn ends."
Celestial_Sword_of_the_Phoenix_Experienced = Item(card_id=9878, title='Celestial Sword of the Phoenix', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), Keitaku], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Pure_Strike_Blade = Item(card_id=9879, title='Pure Strike Blade', force=5, chi=1, gold_cost=6, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card: Ranged 5 Attack.'
The_String_of_the_Colonies = Item(card_id=9880, title='The String of the Colonies', force=0, chi=0, gold_cost=3, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has <b>Conqueror</b>.'
The_Victor = Item(card_id=9881, title='The Victor', force=4, chi=0, gold_cost=6, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Melee and Ranged Attacks targeting this Personality have -5 strength.'
Vanquishers_Armor = Item(card_id=9882, title="Vanquisher's Armor", force=5, chi=0, gold_cost=7, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After this card enters play: Create a +2F/+1C <b>Weapon</b> Item and attach it to this Personality <i>(if legal)</i>.'
Vanquishers_Blades = Item(card_id=9883, title="Vanquisher's Blades", force=4, chi=1, gold_cost=7, focus_value=4, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])