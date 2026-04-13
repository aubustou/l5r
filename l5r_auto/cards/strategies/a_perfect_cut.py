from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow your target unbowed Fortification at this battlefield. Move home a target enemy Personality. Bow his unit as it moves.'
Needed_at_the_Wall = Strategy(card_id=5527, title='Needed at the Wall', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition])