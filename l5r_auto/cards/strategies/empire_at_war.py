from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Castle, Terrain
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'This Province has +4 strength.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Bridging_the_Gap = Strategy(card_id=1140, title='Bridging the Gap', focus_value=4, keywords=[Castle, Terrain], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])