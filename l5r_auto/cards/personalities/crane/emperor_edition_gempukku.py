from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Courtier, Experienced, Imperial, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Political Open:</b> Take the Imperial Favor.'
Doji_Dainagon_Experienced = Personality(card_id=10221, title='Doji Dainagon', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Unique, Courtier, Experienced('1'), Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])