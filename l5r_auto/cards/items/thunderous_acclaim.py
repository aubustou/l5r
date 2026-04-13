from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Bow, Courage, Destined, HeavyWeapon, Jade, Ninja, OneHanded, Peasant, Polearm, Reserve, Spear, Sword, Tessen, TwoHanded, Weapon
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
"Your Personalities with this Personality's Family Name enter play for 1 less Gold."
Box_of_Secrets = Item(card_id=12353, title='Box of Secrets', force=0, chi=0, gold_cost=1, focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(You may Equip a Reserve attachment, if it would be opposed, as a Battle action.)</i><br>After this Item enters play, if the last action another player took destroyed one of your cards, you may take an additional action.<br><b>Battle, :bow::</b> Melee 2 Attack.'
Fang_of_Vengeance = Item(card_id=12354, title='Fang of Vengeance', force=2, chi=1, gold_cost=4, focus_value=2, keywords=[Reserve, Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Repeatable Interrupt: Discard a Courage card to give a Fear effect +2 or -2 strength.)</i> <br><b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>.'
Flawless_Naginata = Item(card_id=12355, title='Flawless Naginata', force=3, chi=2, gold_cost=6, focus_value=0, keywords=[Courage, Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Will not attach to a Shadowlands Personality. This Personality has +1PH. After your turn begins, give this Weapon a +1F/+1C token.'
Inevitable_Victory = Item(card_id=12356, title='Inevitable Victory', force=0, chi=0, gold_cost=4, focus_value=3, keywords=[Destined, Weapon, HeavyWeapon, Jade, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"Equips to Akodo Kano for 1 less Gold. You may use this Personality's Tactical Advantage ability as an Engage."
Kanos_Tessen = Item(card_id=12357, title="Kano's Tessen", force=2, chi=0, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Tessen], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(A Personality may only have one Weapon.)</i> <br><b>Battle, :bow::</b> Ranged 3 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 3 or lower Force)</i>.'
Master_Bowmans_Yumi = Item(card_id=12358, title="Master Bowman's Yumi", force=3, chi=0, gold_cost=6, focus_value=2, keywords=[Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'As a Focus Effect, after a player wins the duel, they may discard a card to draw a card.<br>This Item has +1F/+1C while this Personality has <b>another</b> Matched Daisho or you have <b>Compassion</b>. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>'
Matched_Daisho = Item(card_id=12359, title='Matched Daisho', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Item enters play, lose 3 Honor.<br><b>Ninja Battle, :bow::</b> Bow a target enemy Personality with a Poison token or without abilities.'
Poisoned_Shuriken = Item(card_id=12360, title='Poisoned Shuriken', force=2, chi=1, gold_cost=3, focus_value=3, keywords=[Weapon, Ninja, OneHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Will only attach to an Infantry Personality. This Personality cannot gain Cavalry. Cavalry Personalities may not move to oppose this Personality in the Engage Segment.'
Reinforced_Yari = Item(card_id=12361, title='Reinforced Yari', force=4, chi=0, gold_cost=7, focus_value=3, keywords=[Weapon, Spear, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<i>(A Personality can only have one Armor.)</i> <br><b>Interrupt:</b> Negate the action's Force penalties on all cards in this unit."
Shield_of_the_Honored_Soul = Item(card_id=12362, title='Shield of the Honored Soul', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"Your deck may include four copies of this Item. After it attaches, dishonor its Personality.<br><b>Battle, :bow::</b> Fear 2 that may target Items and Spells, and may not be increased or combined except with other Swordcatchers. Return any attachments this Fear bowed to their owner's hand."
Swordcatcher = Item(card_id=12363, title='Swordcatcher', force=2, chi=1, gold_cost=3, focus_value=2, keywords=[Weapon, OneHanded, Peasant], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])