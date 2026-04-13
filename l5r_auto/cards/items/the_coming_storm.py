from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Bow, Destined, HeavyWeapon, Jade, Mempo, OneHanded, Polearm, Reserve, Staff, Sword, TwoHanded, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
"Cannot attach to a Scorpion Clan Personality. Equips to a Mantis Clan Personality for 1 less Gold. This Personality has <b>Tactician</b>.<br><b>Interrupt, :bow::</b> Negate an action from a Fate card with the same Focus Value as a card discarded by this Personality's Tactical Advantage action this turn."
Aramasus_Mask = Item(card_id=11798, title="Aramasu's Mask", force=0, chi=0, gold_cost=3, focus_value=3, keywords=[Mempo], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after you Equip a Destined card.)</i>'
Awakened_Naginata = Item(card_id=11799, title='Awakened Naginata', force=3, chi=2, gold_cost=7, focus_value=3, keywords=[Destined, Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Give a target enemy Follower or Personality -4F.'
Bishamons_Bow = Item(card_id=11800, title="Bishamon's Bow", force=0, chi=0, gold_cost=2, focus_value=3, keywords=[Weapon, Bow, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Bow a target enemy card.'
Bo_of_Ritual_Blessings = Item(card_id=11801, title='Bo of Ritual Blessings', force=3, chi=2, gold_cost=8, focus_value=4, keywords=[Weapon, Staff, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Jiramus_Wakizashi = Item(card_id=11802, title="Jiramu's Wakizashi", force=1, chi=0, gold_cost=2, focus_value=2, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Give a target enemy Follower or Personality -2F.'
Kaiu_Axe = Item(card_id=11803, title='Kaiu Axe', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Weapon, HeavyWeapon, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Personality has +1PH.<br><b>Battle:</b> Fear 2 <i>(Bow a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Kikko = Item(card_id=11804, title='Kikko', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Battle, :bow::</b> Ranged 3 Attack, or Ranged 4 Attack if the target is Shadowlands <i>(Destroy a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Ranged Attack's strength)</i>."
Osanowos_Bow = Item(card_id=11805, title="Osano-wo's Bow", force=1, chi=0, gold_cost=5, focus_value=3, keywords=[Weapon, Bow, Jade, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After this Personality wins a duel, give this Item a +1F token.'
Singing_Blade = Item(card_id=11806, title='Singing Blade', force=1, chi=1, gold_cost=2, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 4 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 4 or lower Force)</i>.'
Soheis_Ono = Item(card_id=11807, title="Sohei's Ono", force=2, chi=1, gold_cost=7, focus_value=2, keywords=[Weapon, HeavyWeapon, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Battle, :bow::</b> Fear equal to this Personality's Chi that may target a Personality with Followers <i>(Bow a target enemy Follower or Personality with Force equal to or lower than the Fear's strength)</i>."
Tested_Blade = Item(card_id=11808, title='Tested Blade', force=2, chi=1, gold_cost=5, focus_value=3, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(You may Equip a Reserve attachment, if it would be opposed, as a Battle action.)</i><br>After you Equip this Item, you may take an additional action.'
Untested_Blade = Item(card_id=11809, title='Untested Blade', force=1, chi=1, gold_cost=2, focus_value=4, keywords=[Reserve, Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])