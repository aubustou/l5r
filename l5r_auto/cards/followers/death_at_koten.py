from __future__ import annotations
from .common import Follower
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'Can only attach to a Courtier. <br><b>Limited, :bow::</b> Straighten a target Personality with a Political ability.'
Court_Attendants = Follower(card_id=1535, title='Court Attendants', force=1, chi=0, gold_cost=1, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])