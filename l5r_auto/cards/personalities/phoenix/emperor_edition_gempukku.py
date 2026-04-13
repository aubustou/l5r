from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Cavalry, Experienced, Fenghuang, Fire, Nonhuman, Shugenja, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Open:</b> If Kunji is honorably dead: Bring it into play, ignoring costs if you are a Phoenix Clan player.'
Kunji_Experienced = Personality(card_id=10225, title='Kunji', force=3, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[PhoenixClan], keywords=[Cavalry, Unique, Experienced('1'), Fenghuang, Fire, Nonhuman, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])