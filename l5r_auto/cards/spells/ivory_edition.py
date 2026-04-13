from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Earth, Void
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle, :bow::</b> Move your target Personality home.'
Ancestral_Aid = Spell(card_id=11275, title='Ancestral Aid', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Earth Battle, :bow::</b> Fear with strength equal to this Shugenja's Chi, plus 1 if he is Earth. <i>(Bow a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Fear's strength)</i>"
In_Awe_of_the_Earth = Spell(card_id=11276, title='In Awe of the Earth', gold_cost=0, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Void Battle/Open, :bow::</b> Give this Shugenja a Force bonus equal to half his Chi, rounded up.'
Overwhelming_Power = Spell(card_id=11277, title='Overwhelming Power', gold_cost=1, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])