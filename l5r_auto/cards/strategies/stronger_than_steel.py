from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow your target unbowed Personality with 3 or more Personal Honor. Ranged Attack with strength equal to his Personal Honor, plus 2 if he is a Tactician.'
A_Lions_Roar = Strategy(card_id=45, title="A Lion's Roar", focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])