from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import DiamondEdition, IvoryEdition, LotusEdition, ModernEdition, TwentyFestivalsEdition
'<b>Open, :g1::</b> Lose 1 Honor. Target a Personality. His controller may discard a card. If he does, draw a card. If he does not, bow the Personality.'
Men_of_Cunning = Strategy(card_id=5024, title='Men of Cunning', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, DiamondEdition, ModernEdition])