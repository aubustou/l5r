from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Fire, Void, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle:</b> If this Shugenja is unbowed, bow him unless he is Water: In turn order, each player who now controls a unit in the current enemy army targets and moves home one of his units there.'
Fury_of_the_Sea = Spell(card_id=2745, title='Fury of the Sea', gold_cost=1, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Attaches to a Fire or Void Shugenja paying 1 less Gold.<br>This Personality has +2F.<br><b>Battle:</b> Bow this Shugenja: Ranged 5 Attack.'
Tempest_of_Flame = Spell(card_id=7866, title='Tempest of Flame', gold_cost=4, focus_value=2, keywords=[Fire, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])