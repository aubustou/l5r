from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Tattooed
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Negate Fear effects targeting this Follower.<br><b>Battle:</b> Fear 2 <i>(Bow a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>.'
Kikage_Zumi_Initiates = Follower(card_id=4348, title='Kikage Zumi Initiates', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Tattooed], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])
'<b>Battle:</b> Fear 4 that cannot target a Cavalry card <i>(Bow a target enemy Follower, or Personality without Followers, with 4 or lower Force)</i>.'
The_White_Guard = Follower(card_id=8427, title='The White Guard', force=3, chi=0, gold_cost=7, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])