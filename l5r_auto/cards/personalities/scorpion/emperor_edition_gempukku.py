from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Experienced, Ninja, Shadowspawn, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Target a card in a province: Discard it. Refill the province face-up.'
Shosuro_Hawado_Experienced_2 = Personality(card_id=10226, title='Shosuro Hawado', force=4, chi=3, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Experienced('2'), Unique, Ninja, Shadowspawn], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])