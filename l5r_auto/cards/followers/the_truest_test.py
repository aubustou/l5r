from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Nonhuman, Shadowlands, Undead, Yojimbo
from l5r_auto.legality import EmperorEdition, IvoryEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow one of your Followers or Personalities in this army to straighten a target Follower or Personality in this army.'
Devoted_Yojimbo = Follower(card_id=1992, title='Devoted Yojimbo', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=2, keywords=[Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])
'You may Equip this Follower from your discard pile. <br>After you Equip this Follower, lose 3 Honor.'
The_Desiccated = Follower(card_id=8028, title='The Desiccated', force=3, chi=0, gold_cost=4, focus_value=1, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, SamuraiEdition, ModernEdition])
'<b>Open, :bow::</b> If this Personality is a Shugenja, straighten him.'
Tsukaisagasu = Follower(card_id=8779, title='Tsukai-sagasu', force=1, chi=0, gold_cost=3, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, SamuraiEdition, ModernEdition])