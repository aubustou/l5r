from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import DiamondEdition, GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Political Open:</b> Target your Human Personality with neither Samurai nor Shugenja, even if he is in a Province. Permanently give him +1PH and either Samurai or Shugenja. <i>(Shugenja may attach and cast Spells.)</i>'
Gempukku = Strategy(card_id=2788, title='Gempukku', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, DiamondEdition, ModernEdition])