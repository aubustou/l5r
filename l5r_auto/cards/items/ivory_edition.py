from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Destined, Experienced, Knife, OneHanded, Polearm, Spear, Sword, TwoHanded, Unique, Weapon
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Battle, :bow::</b> Reduce the Force of a target enemy Follower or Personality by this Personality's Chi."
Akodo_Kaiken = Item(card_id=11247, title='Akodo Kaiken', force=1, chi=1, gold_cost=3, focus_value=4, keywords=[Weapon, Knife, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Crab Clan Personality. After you Equip this Item, gain 2 Honor. <br><b>Tireless Battle/Open:</b> Straighten this Personality, and straighten his attachments if he is defending.'
Ancestral_Armor_of_the_Crab_Clan_Experienced = Item(card_id=11248, title='Ancestral Armor of the Crab Clan', force=3, chi=0, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Crane Clan Personality. After you Equip this Item, gain 2 Honor. This Personality may Lobby as an <b>Open</b> action. After this Personality Lobbies, gain 1 Honor.'
Ancestral_Armor_of_the_Crane_Clan_Experienced = Item(card_id=11249, title='Ancestral Armor of the Crane Clan', force=2, chi=1, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Dragon Clan Personality. After you Equip this Item, gain 2 Honor. <br><b>Battle/Open, :bow::</b> Straighten your target Ring.'
Ancestral_Armor_of_the_Dragon_Clan_Experienced = Item(card_id=11250, title='Ancestral Armor of the Dragon Clan', force=2, chi=1, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Lion Clan Personality. After you Equip this Item, gain 2 Honor. <br><b>Battle, :bow::</b> If he would be opposed, move a target Personality at any location to this battlefield. Straighten his unit if you do not control him.'
Ancestral_Armor_of_the_Lion_Clan_Experienced = Item(card_id=11251, title='Ancestral Armor of the Lion Clan', force=3, chi=0, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Mantis Clan Personality. After you Equip this Item, gain 2 Honor. <br><b>Open, :bow::</b> Straighten your target Holding.'
Ancestral_Armor_of_the_Mantis_Clan_Experienced = Item(card_id=11252, title='Ancestral Armor of the Mantis Clan', force=3, chi=0, gold_cost=8, focus_value=4, keywords=[Armor, Experienced("Yoritomo's Armor"), Unique], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Phoenix Clan Personality. After you Equip this Item, gain 2 Honor. <br><b>Battle/Open, :bow::</b> Another player may discard a Spell or Kiho from his hand. If he does not, he must target and bow one of his unbowed Personalities.'
Ancestral_Armor_of_the_Phoenix_Clan_Experienced = Item(card_id=11253, title='Ancestral Armor of the Phoenix Clan', force=2, chi=1, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Scorpion Clan Personality. After you Equip this Item, another player loses 2 Honor. <br><b>Limited,:bow::</b> Target a Personality. Bow him if he is dishonorable. Dishonor him.'
Ancestral_Armor_of_the_Scorpion_Clan_Experienced = Item(card_id=11254, title='Ancestral Armor of the Scorpion Clan', force=2, chi=1, gold_cost=8, focus_value=4, keywords=[Armor, Experienced("Shoju's Armor"), Unique], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"Can only attach to a Spider Clan Personality. After you Equip this Item, gain 2 Honor. Does not count towards a Personality's maximum number of Weapons. <br><b>Battle, :bow::</b> Fear 4."
Ancestral_Armor_of_the_Spider_Clan = Item(card_id=11255, title='Ancestral Armor of the Spider Clan', force=3, chi=0, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Weapon], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Unicorn Clan Personality. After you Equip this Item, gain 2 Honor.<br><b>Interrupt, :bow::</b> The action cannot move Personalities.'
Ancestral_Armor_of_the_Unicorn_Clan_Experienced = Item(card_id=11256, title='Ancestral Armor of the Unicorn Clan', force=3, chi=0, gold_cost=8, focus_value=4, keywords=[Armor, Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Personality has +1PH. <br><b>Battle:</b> Fear 2 <i>(Bow a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
DoMaru = Item(card_id=11257, title='Do-Maru', force=1, chi=0, gold_cost=2, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 3 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 3 or lower Force)</i>.'
Exquisite_Nagamaki_of_the_Fox_Clan = Item(card_id=11258, title='Exquisite Nagamaki of the Fox Clan', force=1, chi=2, gold_cost=5, focus_value=3, keywords=[Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Personality has +1PH. <br><b>Battle:</b> Fear 3.'
Haramakido = Item(card_id=11259, title='Haramaki-do', force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Heavy_Yari = Item(card_id=11260, title='Heavy Yari', force=3, chi=1, gold_cost=6, focus_value=2, keywords=[Weapon, Spear, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Light_Yari = Item(card_id=11261, title='Light Yari', force=2, chi=1, gold_cost=5, focus_value=2, keywords=[Weapon, Spear, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This Personality has <b>Conqueror</b> <i>(A Conqueror's unit doesn't bow after battle)</i>."
Oriole_Katana = Item(card_id=11262, title='Oriole Katana', force=1, chi=1, gold_cost=3, focus_value=3, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Personality has +1PH. You may use rulebook Favor abilities two times per turn. When this Personality Lobbies, add his Personal Honor to the Family Honor check. He may Lobby even if you have already Lobbied once this turn.'
Regal_Furisode = Item(card_id=11263, title='Regal Furisode', force=0, chi=0, gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Fear 2 <i>(Bow a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Reinforced_Parangu = Item(card_id=11310, title='Reinforced Parangu', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i><i>(Draw a card after you Equip a Destined card.)</i></i>'
Utakus_Destiny = Item(card_id=11264, title="Utaku's Destiny", force=2, chi=1, gold_cost=4, focus_value=3, keywords=[Destined, Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])