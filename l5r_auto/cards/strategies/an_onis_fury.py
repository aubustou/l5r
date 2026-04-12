from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Political
from l5r_auto.legality import GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle:</b> Fear with strength equal to the number of your Shadowlands Personalities at the current battlefield.'
Everpresent_Fear = Strategy(card_id=2392, title='Everpresent Fear', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, ModernEdition])
'<b>Political Open:</b> Target a Personality. Personalities his controller Recruits <i>(this turn)</i> with greater Personal Honor than the target has now are dishonored before they enter play.'
The_Company_You_Keep = Strategy(card_id=7990, title='The Company You Keep', focus_value=4, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, ModernEdition])