from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Forest, Maho, Pearl, Ritual, Thunder, Void, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Reaction:</b> After an action resolves, bow this card and target one of your Rings the action bowed: Straighten the Ring. If this Shugenja is Void, you may destroy this card; if you did, you may use the Ring's base abilities an additional time this turn."
Centering_the_Soul = Spell(card_id=1277, title='Centering the Soul', gold_cost=0, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Once per game: Give this Personality a permanent Force bonus raising his Force to equal his base Gold Cost. Permanently give him <b><b>Shadowlands &#149; Nonhuman &#149; Oni</b></b>. Lose 2 Honor.'
Damning_Ceremony = Spell(card_id=1808, title='Damning Ceremony', gold_cost=4, focus_value=1, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja and destroy this card: Search your Fate deck for a non-Unique Spell that must share a keyword with the performer unless he is Void, show it, and put it in your hand.'
Delving_into_History = Spell(card_id=1945, title='Delving into History', gold_cost=0, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After this card enters play, if this Shugenja is Air: Each other player loses 1 Honor.<br><b>Open:</b> Destroy this card and target a Personality: The performing Shugenja copies one of the target's abilities which does not copy abilities."
Extending_Influence = Spell(card_id=2420, title='Extending Influence', gold_cost=2, focus_value=1, keywords=[Air], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Air Shugenja have +1C.<br><b>Limited:</b> Bow one or more of your performing Shugenja with 10 or greater total Chi, and remove this card from the game: Create a province to the left of your leftmost province which permanently does not hold Dynasty cards.'
Illusory_Defense = Spell(card_id=3666, title='Illusory Defense', gold_cost=8, focus_value=2, keywords=[Air, Ritual], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While this Shugenja is Earth, your Spirits contribute Force to their army even while bowed.<br><b>Battle:</b> Even if this unit is not at the current battlefield, bow your performing Spirit and target an enemy card: Bow it.'
Incite_the_Phantoms = Spell(card_id=3732, title='Incite the Phantoms', gold_cost=0, focus_value=2, keywords=[Earth, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target an enemy card: Bow it. If this Shugenja is Earth, gain 2 Honor.'
Inescapable_Snare = Spell(card_id=3738, title='Inescapable Snare', gold_cost=0, focus_value=4, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While this Shugenja is Nonhuman, he has +2F.<br><b>Open:</b> Give this Shugenja -2F: He changes shape. Give him <b>Cavalry</b>.<br><b>Battle:</b> Give this Shugenja -2F: Ranged 6 Attack.'
Maras_Touch = Spell(card_id=4833, title="Mara's Touch", gold_cost=2, focus_value=3, keywords=[Pearl], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"While this Shugenja is Fire, he has <b>Duelist</b>.<br><b>Battle:</b> If this Shugenja is unbowed, bow this card and target an enemy Personality: This Shugenja duels him. Destroy a card without attachments in the unit of the duel's loser."
Ochiais_Bravery = Spell(card_id=5666, title="Ochiai's Bravery", gold_cost=3, focus_value=4, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Even if this unit is not at the current battlefield, bow this Shugenja, choose your performing Spirit, and target an enemy Personality: Move him home. If this Shugenja is Water, gain 1 Honor.'
Sudden_Guardian = Spell(card_id=7612, title='Sudden Guardian', gold_cost=0, focus_value=2, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja unless he is Thunder, and target a Personality: After the next time <i>(this turn)</i> he assigns or an action resolves which moved him to a battlefield, bow him.'
The_Menacing_Sky = Spell(card_id=8219, title='The Menacing Sky', gold_cost=2, focus_value=2, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, you may attach this card to one of your Water Shugenja, ignoring Gold cost.<br>This Shugenja has +2F.<br><b>Battle:</b> Bow this card and target an enemy Personality or Follower: Reduce its Force to 0.'
The_Swell_of_Strength = Spell(card_id=8366, title='The Swell of Strength', gold_cost=3, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])