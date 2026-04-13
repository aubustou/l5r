from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Armor, Earth, Fire, Maho, Thunder, Void, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Earth Remote Battle, :bow::</b> Give your target defending Spirit +3F and <b>Elite</b> <i>(Elite cards contribute Force even if bowed)</i>.'
Anchored_in_Earth = Spell(card_id=10346, title='Anchored in Earth', gold_cost=0, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Maho Remote Battle:</b> Bow this Shugenja and destroy your target Personality or Follower to create two consecutive Ranged Attacks, each with strength equal to half your target's Force, rounded down."
Blood_Wave = Spell(card_id=10348, title='Blood Wave', gold_cost=0, focus_value=3, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After this Spell attaches, choose an element keyword <i>(Air, Earth, Fire, Water, Void)</i> in this Shugenja's keywords or text. While this Spell remains attached, replace all instances of that keyword on this Shugenja with a different element keyword that you choose now."
Blood_of_Isawas_Tribe = Spell(card_id=10347, title="Blood of Isawa's Tribe", gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow this card and give the current battlefield's province a bonus, or a penalty if you are defending, from 1 up to its current strength: Give this Shugenja an equal Force bonus. Negate his next bowing or movement from other players' cards' effects if he is Earth."
Earths_Protection = Spell(card_id=10349, title="Earth's Protection", gold_cost=0, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Stronghold has +1 Gold Production for each Spirit you control.'
Opening_the_Veil = Spell(card_id=10350, title='Opening the Veil', gold_cost=0, focus_value=2, keywords=[Earth, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle/Open:</b> Bow this card and target a Personality: Negate all Force penalties on him and other players' cards' effects that prevent him performing actions."
Path_to_Inner_Peace = Spell(card_id=10351, title='Path to Inner Peace', gold_cost=0, focus_value=4, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Bow this card and target one face-down card in a province, or one or two such cards if this Shugenja is Void: Turn the targets face-up.'
Read_the_Essence = Spell(card_id=10352, title='Read the Essence', gold_cost=0, focus_value=3, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Shugenja has <b>Duelist</b> while he is Fire.<br><b>Battle/Open:</b> Remove a non-Ring card in any discard pile from the game, and target a Personality: Give him +3F or -3F.'
Scorching_Lash = Spell(card_id=10353, title='Scorching Lash', gold_cost=3, focus_value=4, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy this card and target an attacking Personality: Give him <b>Elite</b> <i>(Elite cards contribute Force even if bowed)</i>. He does not contribute Force while unbowed. If this Shugenja is Air, gain 2 Honor.'
The_Skys_Barrier = Spell(card_id=10354, title="The Sky's Barrier", gold_cost=0, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"This Personality has +4F.<br><b>Reaction:</b> After an action targets a card in this unit, bow this card: Bow the action's performers <i>(if any)</i> after the action resolves."
The_Thunderers_Protection = Spell(card_id=10355, title="The Thunderer's Protection", gold_cost=6, focus_value=1, keywords=[Armor, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Bow this Shugenja, destroy this card, and target a Personality who must be non-Unique unless this Shugenja is Void: Show cards from the top of the target's controller's Dynasty deck until you show a Personality or you show all cards in the deck. If you showed a Personality, overlay him on the target."
Unbound_Essence = Spell(card_id=10356, title='Unbound Essence', gold_cost=5, focus_value=0, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After your Ring enters play, bow this card: Look at the top three cards of your Dynasty or Fate deck. Put them back in any order.'
Witness_the_Untold = Spell(card_id=10357, title='Witness the Untold', gold_cost=0, focus_value=2, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])