from __future__ import annotations
from .common import Follower
from l5r_auto.legality import DiamondEdition, GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle, :bow:, :g*::</b> Destroy this Follower. Search your Fate deck for a non-Unique Follower not named Karo. Equip it for 3 less Gold.'
Karo = Follower(card_id=4283, title='Karo', force=0, chi=0, gold_cost=3, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, DiamondEdition, ModernEdition])