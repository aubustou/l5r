from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Bow, Courage, Cursed, Destined, Expendable, Gaijin, Kharmic, Knife, Nemuranai, Ninja, OneHanded, Peasant, Staff, Sword, TwoHanded, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'This Personality has <b>Resilient</b>.<br><b>Interrupt:</b> After you Equip this Item, rehonor this Personality, and you may target and rehonor another Personality.'
Aranais_Armor = Item(card_id=11634, title="Aranai's Armor", force=2, chi=0, gold_cost=4, focus_value=1, keywords=[Armor, Destined], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Interrupt:</b> Discard a Courage card to give a Fear effect +2 or -2 strength.)</i>'
Aranais_Kama = Item(card_id=11635, title="Aranai's Kama", force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Courage, Weapon, OneHanded, Peasant], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after your Expendable card is destroyed.)</i><br><b>Battle, :bow::</b> Ranged 3 Attack.'
Crude_Daikyu = Item(card_id=11636, title='Crude Dai-kyu', force=0, chi=0, gold_cost=3, focus_value=2, keywords=[Expendable, Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after you Equip a Destined card.)</i><br>After this Weapon enters your discard pile from play, put it back into your hand.'
Ensorcelled_Longsword = Item(card_id=11637, title='Ensorcelled Longsword', force=2, chi=1, gold_cost=5, focus_value=4, keywords=[Destined, Weapon, Gaijin, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card to draw a card.)</i> <br>In a duel, you may focus this Item from your discard pile and remove it from the game after the focused cards are discarded.'
Heirloom_Tanto = Item(card_id=11638, title='Heirloom Tanto', force=1, chi=1, gold_cost=2, focus_value=4, keywords=[Kharmic, Weapon, Knife, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After this Item enters play, lose 1 Honor.<br><b>Ninja Interrupt, :bow::</b> After each time your action targets an enemy Follower or Personality, give it -2F until after the action resolves.'
Hidden_Dagger = Item(card_id=11639, title='Hidden Dagger', force=2, chi=1, gold_cost=3, focus_value=1, keywords=[Weapon, Ninja, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"Card effects will not straighten this Item.<br><b>Political Open, :bow::</b> Give this Item a number of <b>Favor </b>tokens equal to this Personality's Personal Honor.<br><b>Political Open, :bow::</b> Target a Personality. Discard two Favor tokens from this Item to negate his next straightening this game or five Favor tokens from it to bow him."
Official_Sanction = Item(card_id=11640, title='Official Sanction', force=0, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Interrupt:</b> Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br><b>Battle, :bow::</b> Melee 2 Attack. Lose 1 Honor.'
Opportune_Weapon = Item(card_id=11641, title='Opportune Weapon', force=2, chi=0, gold_cost=4, focus_value=1, keywords=[Courage, Weapon, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'You may Equip this Item as an Engage action.<br><b>Battle:</b> Fear 1, or Fear 2 if you Equipped this Item during this battle.'
Shikomizue = Item(card_id=11642, title='Shikomizue', force=2, chi=1, gold_cost=3, focus_value=2, keywords=[Weapon, OneHanded, Staff, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<i>(Repeatable Interrupt: Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br>Before this Personality wins a duel, negate the loser's destruction. After this Personality wins a duel, gain 1 Honor."
Shinai = Item(card_id=11643, title='Shinai', force=1, chi=1, gold_cost=4, focus_value=2, keywords=[Courage, Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Engage:</b> Give a target enemy card -1F.<br><b>Battle:</b> Ranged 1 Attack.<br><b>Battle:</b> Fear 1.<br><b>Battle, :bow::</b> Straighten this Personality.'
Staff_of_the_Rajas_Court = Item(card_id=11644, title="Staff of the Raja's Court", force=2, chi=1, gold_cost=5, focus_value=4, keywords=[Weapon, Nemuranai, Staff, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Invest :g1::</b> Search your Fate deck for a Stockpiled Weapon, show it, and put it in your hand.'
Stockpiled_Weapon = Item(card_id=11645, title='Stockpiled Weapon', force=2, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"On your turn, you must declare an Attack Phase and assign this Personality to attack, if able.<br><b>Battle, :bow::</b> Destroy a target enemy card with Force less than or equal to this Item's, and no attachments. Give this Item a +1F token."
Toshigokus_Blade = Item(card_id=11646, title="Toshigoku's Blade", force=3, chi=-1, gold_cost=7, focus_value=1, keywords=[Weapon, Cursed, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])