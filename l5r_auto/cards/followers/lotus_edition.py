from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Nonhuman, Pack, Ratling, Shadowlands, Undead
from l5r_auto.legality import DiamondEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'After this Follower enters play from your hand, you may draw an additional card when this turn ends.<br><b>Battle, :bow::</b> Ranged 2 Attack.'
Ashigaru_Archers = Follower(card_id=608, title='Ashigaru Archers', force=0, chi=0, gold_cost=2, focus_value=1, keywords=[Ashigaru], traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, GoldEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
'This Follower has +2F while attached to a Ratling.<br><b>Battle:</b> Ranged 2 Attack.'
Ratling_Archers = Follower(card_id=6166, title='Ratling Archers', force=1, chi=0, gold_cost=3, focus_value=2, keywords=[Nonhuman, Pack, Ratling], traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
'After you Equip this Follower, lose 2 Honor. <br><b>Battle:</b> Fear 3 <i>(Bow a target enemy Follower, or Personality without Followers, with 3 or lower Force)</i>.'
Skeletal_Troops = Follower(card_id=7281, title='Skeletal Troops', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, ImperialEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])