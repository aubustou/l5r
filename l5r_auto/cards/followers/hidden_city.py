from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Nonhuman, Oni, Shadowlands
from l5r_auto.legality import DiamondEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Can only attach to a Samurai.<br><b>Battle, :bow::</b> Ranged 3 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 3 or lower Force)</i>.'
Expert_Archers = Follower(card_id=2412, title='Expert Archers', force=2, chi=0, gold_cost=4, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, DiamondEdition, ModernEdition])
'After this Follower enters play, lose 3 Honor. <br>If this Follower has <b>7</b> Force or less, after a Follower or Personality is destroyed at this battlefield, give this Follower a +1F token.'
Fudoshi = Follower(card_id=2723, title='Fudoshi', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, DiamondEdition, ModernEdition])