from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Fire, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle/Open:</b> If this Shugenja shares an element keyword with a Ring you control, either straighten the Ring or this Shugenja.'
All_Within_the_World = Spell(card_id=326, title='All Within the World', gold_cost=0, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This Shugenja has +5F.<br><b>Battle:</b> Bow this card: Ranged 5 Attack, or Ranged 6 Attack if this Shugenja is Fire.'
Channeling_the_Fallen = Spell(card_id=1296, title='Channeling the Fallen', gold_cost=8, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Destroy this card, bow this Shugenja unless he is Fire, and target an enemy card without attachments in a unit whose Personality has Force lower than or equal to your Shugenja's Force or Chi: Destroy the enemy card."
Hunger_of_the_Fire = Spell(card_id=3517, title='Hunger of the Fire', gold_cost=0, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])