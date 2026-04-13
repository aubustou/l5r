from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Camel, Cavalry, ClaySoldier, Djinn, Elephant, Fire, Fudo, Gaijin, Gaijin149Yodotai, Legionnaire, Monk, Nonhuman, SpawnOfVritra, Spirit, Yodotai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'After this Follower enters play, lose 2 Honor.<br>Legionnaires in this unit have +1F.'
Aulus = Follower(card_id=10687, title='Aulus', force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Gaijin149Yodotai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will only attach to a Human. This Personality has <b>Cavalry</b>.<br><b>Home Battle:</b> Move this unit to the current battlefield if it would be opposed there.'
Camel_Mounts = Follower(card_id=10682, title='Camel Mounts', force=3, chi=0, gold_cost=6, focus_value=2, keywords=[Cavalry, Camel, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Invest :g5:: Give this Follower two +1F tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Clay_Kshatriya = Follower(card_id=10678, title='Clay Kshatriya', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[ClaySoldier, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will only attach to a Human. Cards in this unit have <b>Cavalry</b>.<br>Melee and Ranged Attacks targeting cards in this unit have -2 strength.'
Elephant_Cavalry = Follower(card_id=10679, title='Elephant Cavalry', force=4, chi=0, gold_cost=8, focus_value=2, keywords=[Cavalry, Elephant, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After this Follower enters play, search your discard pile, then deck, for another Enslaved Djinn. Show it. Put it into your hand.'
Enslaved_Djinn = Follower(card_id=10680, title='Enslaved Djinn', force=2, chi=0, gold_cost=4, focus_value=1, keywords=[Djinn, Fire, Nonhuman, Spirit], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'You may Equip this Follower from your discard pile.'
Frontier_Farmer = Follower(card_id=10681, title='Frontier Farmer', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Personality may not attack.<br><b>Limited, :bow::</b> Dishonor a target Human Personality. Destroy this Follower.'
Kamalakars_Harem = Follower(card_id=10683, title="Kamalakar's Harem", force=0, chi=0, gold_cost=0, focus_value=2, keywords=[Gaijin], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited, :bow::</b> Put a Ring from your discard pile into your hand. Destroy this Follower.'
Scholarly_Hermit = Follower(card_id=10684, title='Scholarly Hermit', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Fudo, Gaijin, Monk], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will not attach to a Water Personality.<br><b>Battle:</b> Ranged 6 Attack.'
Spawn_of_Vritra = Follower(card_id=10685, title='Spawn of Vritra', force=5, chi=0, gold_cost=8, focus_value=3, keywords=[Nonhuman, SpawnOfVritra], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy Personality or Follower -3F.'
Spitting_Llama = Follower(card_id=10686, title='Spitting Llama', force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Cavalry, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After this Follower enters play, lose 1 Honor and discard a card.<br><b>Engage:</b> Give a target enemy Personality or Follower -2F.'
The_Bestial_Ones = Follower(card_id=10677, title='The Bestial Ones', force=3, chi=0, gold_cost=3, focus_value=2, keywords=[Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'You may include any number of this Follower in your deck.<br>After this Follower enters play, lose 2 Honor.'
Yodotai_Legionnaire = Follower(card_id=10688, title='Yodotai Legionnaire', force=1, chi=0, gold_cost=0, focus_value=1, keywords=[Gaijin, Legionnaire, Yodotai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])