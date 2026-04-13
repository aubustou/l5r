from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'After this Follower enters play from your hand, you may draw an additional card when this turn ends. <br><b>Battle, :bow::</b> Ranged 1 Attack.'
Ashigaru_Spearmen = Follower(card_id=619, title='Ashigaru Spearmen', force=1, chi=0, gold_cost=2, focus_value=1, keywords=[Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
"Crane Clan and Scorpion Clan players Equip this Follower for 2 less Gold. Before your Political action bows this Personality, you may bow this Follower instead, which fulfills the action's costs and conditions of bowing."
Diplomatic_Apprentice = Follower(card_id=2000, title='Diplomatic Apprentice', force=0, chi=0, gold_cost=5, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, SamuraiEdition, DiamondEdition, ModernEdition])