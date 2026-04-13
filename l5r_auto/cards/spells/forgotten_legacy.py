from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Pearl, Political, Thunder, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"This Shugenja has +1F for each Pearl card you control and in your discard piles.<br><b>Battle:</b> Bow this card: Ranged Attack with strength equal to this Shugenja's Chi, plus the number of Pearl cards you control and in your discard piles."
Pearl_of_Rage = Spell(card_id=5903, title='Pearl of Rage', gold_cost=2, focus_value=4, keywords=[Unique, Pearl], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"While this Shugenja is Earth and defending, negate his destruction from other players' cards' effects.<br><b>Battle:</b> Bow this card and target an enemy card without attachments: Bow it. Gain 1 Honor."
The_Mountains_Power = Spell(card_id=8228, title="The Mountain's Power", gold_cost=0, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target an enemy Personality or Follower: Give it -4F.<br><b>Battle:</b> Destroy this card: Ranged 4 Attack with +2 strength if it targets a Follower. If this Shugenja is Thunder and the Ranged Attack destroyed a Follower, Ranged 4 Attack.'
Thunders_Wrath = Spell(card_id=8475, title="Thunder's Wrath", gold_cost=0, focus_value=2, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"While this Shugenja is Air, he straightens during each player's Straighten Phase.<br><b>Open:</b> Bow this Shugenja and target a face-up Personality out of play: Give him +1PH or +1 Gold Cost."
Wind_of_the_Moon = Spell(card_id=9339, title='Wind of the Moon', gold_cost=0, focus_value=2, keywords=[Air, Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])