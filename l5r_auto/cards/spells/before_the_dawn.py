from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Maho, Thunder, Void, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"While this Shugenja is Thunder, he has +1C.<br><b>Thunder Battle, :bow::</b> Ranged Attack with strength equal to this Shugenja's Chi."
A_Dragons_Favor = Spell(card_id=18, title="A Dragon's Favor", gold_cost=0, focus_value=3, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"This Shugenja has +2F and Shadowlands.<br><b>Battle:</b> Remove a target dead Personality in any player's discard pile from the game: Create a 2F/2C/0PH <b>Shadowlands &#149; Undead</b> Personality at the current battlefield. Remove him from the game after this battle's resolution. Lose 2 Honor."
Death_Defeated = Spell(card_id=1898, title='Death, Defeated', gold_cost=2, focus_value=2, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'While this Shugenja is Earth, your provinces have +1 strength.<br><b>Battle/Open:</b> Bow this Shugenja, destroy this card, and target a bowed Personality: Negate his next straightening this game.'
Drawing_on_the_Mountain = Spell(card_id=2236, title='Drawing on the Mountain', gold_cost=0, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'While this Shugenja is Fire, he has +1F.<br><b>Battle:</b> Bow this card and target an enemy attachment: Destroy it.'
Embers_Final_Fire = Spell(card_id=2309, title="Ember's Final Fire", gold_cost=0, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"While this Shugenja is Water, other players' provinces have -1 strength.<br><b>Reaction:</b> After the resolution of an action that moved a Personality to the current battlefield: Give him -4F."
Erosion = Spell(card_id=2363, title='Erosion', gold_cost=0, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"You may attach this card from your discard pile to your Void Shugenja.<br><b>Open:</b> Bow this card and target another player's Personality: You find out his dark secret. Give him <b>Kolat, Ninja, </b>or<b> Shadowlands</b>."
Seek_the_Stain = Spell(card_id=6559, title='Seek the Stain', gold_cost=0, focus_value=3, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'While this Shugenja is Void, your maximum hand size is increased by 1. <br><b>Limited:</b> Bow this card: Look at the top card of any Fate deck. You may destroy this card; if you do, discard the card you looked at.'
The_Tapestry_Perceived = Spell(card_id=8371, title='The Tapestry Perceived', gold_cost=0, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After you Equip this Spell, if this Shugenja is Air, a target player gains or loses 1 Honor. <br><b>Air Open:</b> Bow this Shugenja to target another player's Personality. After the next time <i>(this turn)</i> the target assigns to attack you, gain 1 Honor, or 2 Honor if you control a Temple."
Words_of_Consecration = Spell(card_id=9378, title='Words of Consecration', gold_cost=1, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])