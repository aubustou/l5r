from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import DarkVirtue, Determination
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Dark Virtue Battle:</b> Target your unbowed Samurai Personality. Fear with strength equal to his Force minus 1 <i>(minimum zero)</i>.'
Ruthless_Determination = Strategy(card_id=6415, title='Ruthless Determination', gold_cost=0, focus_value=3, keywords=[DarkVirtue, Determination], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])