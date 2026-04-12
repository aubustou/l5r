from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Gaijin, Nemuranai, Ninja, OneHanded, Shadowlands, Sword, TwoHanded, Water, Weapon
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Limited, :bow::</b> Look at the top three cards of your Fate deck. Put them back in any order.<br><b>Limited, :bow::</b> Draw a card. Destroy this Item.'
Divination_Bowl = Item(card_id=10690, title='Divination Bowl', force=0, chi=0, gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Fudo and Fallen Personalities have -1F while opposing this Item.'
Kshatriya_Artifacts = Item(card_id=10691, title='Kshatriya Artifacts', force=0, chi=1, gold_cost=0, focus_value=1, keywords=[Gaijin], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"The Attacker may not take Engage actions at this Item's battlefield."
Lantern_Oil = Item(card_id=10692, title='Lantern Oil', force=0, chi=0, gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle, :bow::</b> Bow a target Personality with Force equal to or lower than this Personality's."
Lost_Blade_of_the_Maharaja = Item(card_id=10693, title='Lost Blade of the Maharaja', force=3, chi=1, gold_cost=7, focus_value=3, keywords=[Weapon, Gaijin, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"Other players' Terrains will not destroy your Terrains at this Item's battlefield."
Map_of_the_Northern_Colonies = Item(card_id=10694, title='Map of the Northern Colonies', force=0, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After this Item enters play, lose 3 Honor.<br><b>Ninja Battle, :bow::</b> Give a target enemy Personality a -1F/-1C <b>Poison </b>token.'
Red_Hungers_Fang = Item(card_id=10696, title="Red Hunger's Fang", force=2, chi=0, gold_cost=4, focus_value=4, keywords=[Weapon, Ninja, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<i>(A Personality can only have one Weapon.)</i><br>This Item's Force modifier equals this Personality's Personal Honor."
Seppuns_Blessed_Blade = Item(card_id=10695, title="Seppun's Blessed Blade", force=0, chi=2, gold_cost=5, focus_value=2, keywords=[Weapon, Sword, TwoHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'After this Item enters play, lose 2 Honor, create three 1F <b>Nonhuman &#149; Raptor &#149; Shadowlands &#149; Undead &#149; Cavalry</b> Followers, and attach them to your Personalities.'
Shard_of_the_Great_Deaths_Bones = Item(card_id=10697, title="Shard of the Great Death's Bones", force=0, chi=0, gold_cost=3, focus_value=3, keywords=[Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited, :bow::</b> Give this Item a +1F token.'
Translated_Story_of_Shaharazad = Item(card_id=10698, title='Translated Story of Shaharazad', force=0, chi=0, gold_cost=3, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Water Open:</b> Target a non-Unique Weapon attached to this Personality. Copy an ability on it that does not itself copy ability, to this Weapon <i>(until the turn ends)</i>.'
Watersteel_Sword = Item(card_id=10689, title='Watersteel Sword', force=2, chi=1, gold_cost=4, focus_value=2, keywords=[Weapon, Nemuranai, Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])