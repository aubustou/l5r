from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Fire, Kharmic, Maho, Void, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Thunder Battle:</b> Fear 1 <i>(Bow a target enemy Follower, or Personality without Followers, with 1 or lower Force)</i>.<br><b>Thunder Interrupt, :bow::</b> Give a Fear effect +2 strength.'
Fear_the_Thunder = Spell(card_id=11812, title='Fear the Thunder', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Void Interrupt:</b> Negate a Battle action. Destroy this Spell. Remove the caster's unit from the game, keeping all attachments and tokens, and ignoring leaving-play effects. Return it to play before the turn ends, ignoring entering-play costs and effects."
Interrupt_the_Voids_Flow = Spell(card_id=11813, title="Interrupt the Void's Flow", gold_cost=2, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'You may Equip this Spell as an <b>Interrupt</b>.<br><b>Earth Interrupt, :bow::</b> Give a Fear effect, Melee Attack, or Ranged Attack -2 strength, or -3 if this Shugenja is Earth. Destroy this Spell.'
Legacy_of_Tadaka = Spell(card_id=11814, title='Legacy of Tadaka', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"You may not Proclaim Courtiers.<br><b>Air Interrupt, :bow::</b> Reduce each Honor gain from the action <i>(to a minimum of 0)</i> by half this Shugenja's Chi, rounded down."
Look_Into_the_Soul = Spell(card_id=11815, title='Look Into the Soul', gold_cost=0, focus_value=3, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After you Equip this Spell, lose 2 Honor.<br><b>Maho Open, :bow::</b> Target an unbowed Personality. If this Shugenja assigns to attack this turn, the target must assign to defend opposing him, if legal. Destroy this Spell after the target assigns.'
Sinful_Dreams = Spell(card_id=11816, title='Sinful Dreams', gold_cost=2, focus_value=2, keywords=[Maho], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"Attaches to a Fire Shugenja for 1 less Gold.<br><b>Fire Battle:</b> Target your Personality. Ranged Attack equal to his Chi. Destroy this Spell. <i>(Destroy a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Ranged Attack's strength.)</i>"
The_Dragons_Breath = Spell(card_id=11817, title="The Dragon's Breath", gold_cost=3, focus_value=1, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"Invest :g4:: Give this Personality three +1F <b>Fire </b>tokens.<br><b>Fire Battle, :bow::</b> Ranged Attack equal to this Shugenja's Chi, plus 1 if he is Fire."
The_Dragons_Talon = Spell(card_id=11818, title="The Dragon's Talon", gold_cost=5, focus_value=1, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Water Battle, :bow::</b> Bow a target enemy attachment whose Force is less than or equal to this Shugenja's Chi, or his Chi plus 2 if he is Water."
The_Swell_of_the_Storm = Spell(card_id=11819, title='The Swell of the Storm', gold_cost=0, focus_value=2, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Void Open, :bow::</b> Search your Dynasty deck for a non-Unique Personality with your Clan Alignment. Discard a card in one of your Provinces and refill it face-up with the Personality. Destroy this Spell.'
Visions_of_Darkness = Spell(card_id=11820, title='Visions of Darkness', gold_cost=1, focus_value=4, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])