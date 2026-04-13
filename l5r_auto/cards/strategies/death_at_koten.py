from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Political Open:</b> Target your unbowed Courtier. After each time any player assigns, he loses 1 Honor for each unit he assigned, up to three units.'
Civil_Discussion = Strategy(card_id=1397, title='Civil Discussion', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, SamuraiEdition, ModernEdition])