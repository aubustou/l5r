from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Political
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Political Battle:</b> Move home your target Courtier. Give the current Province +3 strength, and if the enemy leader controls a dishonorable Personality at its battlefield, he loses 2 Honor.'
Oppression = Strategy(card_id=5769, title='Oppression', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])