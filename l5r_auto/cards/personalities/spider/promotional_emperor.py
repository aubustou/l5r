from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Cavalry, Samurai, Shadowlands
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After Hirose enters play, lose 1 Honor.'
Daigotsu_Hirose = Personality(card_id=10582, title='Daigotsu Hirose', force=3, chi=2, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[SpiderClan, ShadowlandsFaction], keywords=[Cavalry, Samurai, Shadowlands], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])