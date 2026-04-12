from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Port
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Open:</b> Give your target Personality Naval. Destroy this Holding. <i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i>"
Fortified_Docks = Holding(card_id=2666, title='Fortified Docks', gold_cost=2, keywords=[Port], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])