from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Political
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Political Open:</b> Before the next time this turn a player gains Honor from an action he took, he loses that amount of Honor instead of gaining it.'
Faint_Praise = Strategy(card_id=2442, title='Faint Praise', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])