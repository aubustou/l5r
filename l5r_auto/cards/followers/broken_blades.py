from __future__ import annotations
from .common import Follower
from l5r_auto.legality import GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'If this Personality is ever attacking, destroy this Follower.'
Iron_Defenders = Follower(card_id=3802, title='Iron Defenders', force=3, chi=0, gold_cost=2, focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, ModernEdition])