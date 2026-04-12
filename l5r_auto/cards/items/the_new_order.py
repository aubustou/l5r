from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Bow, Courage, Expendable, HeavyWeapon, Imperial, LoveLetter, OneHanded, Polearm, Siege, Sword, Tessen, Thunder, TwoHanded, Water, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
"This Weapon's Force Modifier is equal to the number of dishonorable Personalities you control, to a maximum of +3F. <br><b>Battle, :bow::</b> Dishonor your target honorable Personality. Straighten a target Personality."
Akumato = Item(card_id=11964, title='Akumato', force=0, chi=0, gold_cost=3, focus_value=3, keywords=[Expendable, Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Item has -3F while it is bowed.<br><b>Siege Battle, :bow::</b> Melee 5 Attack.<br><b>Siege Battle, :bow::</b> Destroy a target Fortification at this battlefield.'
Demolisher = Item(card_id=11957, title='Demolisher', force=3, chi=0, gold_cost=8, focus_value=1, keywords=[Siege], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after your Expendable card is destroyed.)</i>'
Forge_Hammer = Item(card_id=11960, title='Forge Hammer', force=2, chi=0, gold_cost=2, focus_value=3, keywords=[Expendable, Weapon, HeavyWeapon, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Card effects will not move this Personality. Melee and Ranged Attacks targeting this Personality have -2 strength.'
Iron_Armor = Item(card_id=11959, title='Iron Armor', force=2, chi=0, gold_cost=4, focus_value=1, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Home Battle:</b> If this Personality would be opposed, move him to the current battlefield.<br><b>Thunder Battle, :bow::</b> Melee 3 Attack.'
Raiden_OTsuchi = Item(card_id=11961, title='Raiden O-Tsuchi', force=3, chi=0, gold_cost=8, focus_value=2, keywords=[Courage, Weapon, HeavyWeapon, Thunder, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Melee and Ranged Attacks targeting cards in this unit have -1 strength.'
Saikatsu = Item(card_id=11962, title='Saikatsu', force=3, chi=2, gold_cost=5, focus_value=1, keywords=[Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Equips to Matsu Hachiro for 1 less Gold.<br><b>Battle:</b> Fear 2, or Fear 4 if the target is a Follower.'
Takatsume = Item(card_id=11958, title='Takatsume', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Equips to Kakita Daitsu for 1 less Gold.<br><b>Battle, :bow::</b> If your card bowed this Personality this battle, straighten him.'
Taketori = Item(card_id=11956, title='Taketori', force=2, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Equips to a Phoenix Clan Personality for 1 less Gold. This Personality has <b>Cavalry</b> and <b>Tactician</b>. <br><b>Water Battle, :bow::</b> Move this Personality home. Straighten his unit as he moves.'
Tessen_of_the_Tsunami_Legion = Item(card_id=11966, title='Tessen of the Tsunami Legion', force=0, chi=1, gold_cost=6, focus_value=4, keywords=[Weapon, OneHanded, Tessen, Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(This is not an Affection token for Iweko Miaka.)</i><br><b>Open, :bow::</b> Search your discard pile, then Dynasty deck for Iweko Miaka. If she is not dead, discard a card in one of your Provinces and refill it with her, face-up. Discard this Item.'
Token_of_Affection = Item(card_id=11967, title='Token of Affection', force=0, chi=0, gold_cost=0, focus_value=4, keywords=[Imperial, LoveLetter], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Ranged 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>.'
Tsuruchi_Hankyu = Item(card_id=11963, title='Tsuruchi Hankyu', force=1, chi=0, gold_cost=2, focus_value=3, keywords=[Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Equips to Kakita Shinichi for 1 less Gold.<br><b>Interrupt, :bow::</b> If the action is from this Personality, its Fear effects destroy attachments after bowing them.'
Uguisu = Item(card_id=11965, title='Uguisu', force=2, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Invest :g1:: Gain 1 Honor. <i>(Increase the Gold Cost by the Invest cost to get the effect, once.)</i>'
Unfinished_Blade = Item(card_id=11968, title='Unfinished Blade', force=2, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])