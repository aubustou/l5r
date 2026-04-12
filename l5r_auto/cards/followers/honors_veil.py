from __future__ import annotations
from .common import Follower
from l5r_auto.legality import IvoryEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'After you Equip this Follower, gain 1 Honor. <br><b>Political Battle:</b> Bow or straighten a target Personality with lower Personal Honor than this Personality.'
Sparrow_Clan_Aide = Follower(card_id=7396, title='Sparrow Clan Aide', force=2, chi=0, gold_cost=3, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])