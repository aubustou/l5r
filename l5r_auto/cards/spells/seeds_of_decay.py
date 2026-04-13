from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Kami, Maho, Thunder, Void, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Thunder Battle, :bow::</b> Give a target enemy Personality or Follower a Force penalty equal to this Shugenja's Chi. If its Force is now 0 or this Shugenja is Thunder, you may destroy this Spell to take an additional Battle action."
Deafening_Thunder = Spell(card_id=10125, title='Deafening Thunder', gold_cost=0, focus_value=2, keywords=[Thunder], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
"This card enters play paying 1 less Gold for each Ring you control.<br><b>Battle:</b> Destroy this card, bow this Shugenja, destroy him unless he is Void, and target an enemy Personality: His controller may shuffle him and his attachments back into their owners' decks. If he did not choose this, take two additional Battle actions."
Extend_the_Souls_Boundaries = Spell(card_id=10126, title="Extend the Soul's Boundaries", gold_cost=2, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Shugenja has +3F, or +4F while he is Fire.'
Immolation = Spell(card_id=10127, title='Immolation', gold_cost=4, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Even if this card is not at the current battlefield, bow this Shugenja and target one or two Shadowlands Nonhumans: Straighten them.'
Master_of_Beasts = Spell(card_id=10128, title='Master of Beasts', gold_cost=0, focus_value=3, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"If this Shugenja is Earth, he may perform this card's Battle action even if it is in your home.<br><b>Battle:</b> Bow this card and target your Nonhuman Personality: If he would be opposed, move him to the current battlefield. Straighten him if he moved."
Natures_Wrath = Spell(card_id=10129, title="Nature's Wrath", gold_cost=0, focus_value=2, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"If this Shugenja is Water, he may perform this card's Battle action even if it is in your home.<br><b>Battle:</b> Bow this card and target your Personality or Follower: Negate all current effects on it from other players' cards. Negate its <i>(current and new)</i> Force penalties from actions. If it is a Spirit, straighten it."
Peace_of_the_Kami = Spell(card_id=10130, title='Peace of the Kami', gold_cost=2, focus_value=3, keywords=[Kami, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Bow this Shugenja unless he is Air, destroy this card, and target a Kolat, Ninja, Shadowlands, or dishonorable Personality: Bow him.'
Scent_of_Dishonor = Spell(card_id=10131, title='Scent of Dishonor', gold_cost=0, focus_value=2, keywords=[Air], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Destroy this card unless this Shugenja is Void: Remove this Shugenja from the game; his attachments stay attached. Before this turn ends, put his unit into play, ignoring costs, entering-play effects, and restrictions.'
Step_Through_the_Void = Spell(card_id=10132, title='Step Through the Void', gold_cost=0, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Shugenja has <b>Naval</b>.'
Suitengus_Path = Spell(card_id=10133, title="Suitengu's Path", gold_cost=0, focus_value=1, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow this card and target your Earth or Water Shugenja: Straighten him. Gain 1 Honor if he is an Alchemist and opposed.<br><b>Reaction:</b> Before an action resolves, bow this card and target a defending Personality: Negate his movement from the action's effects."
The_Earths_Strength = Spell(card_id=10134, title="The Earth's Strength", gold_cost=0, focus_value=2, keywords=[Earth, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])