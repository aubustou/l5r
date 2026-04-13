from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Cavalry, Naval, Samurai, Thunder
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After Nishima moves as an Engage action, he loses <b>Naval</b>.'
Tsuruchi_Nishima = Personality(card_id=10579, title='Tsuruchi Nishima', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Cavalry, Naval, Samurai, Thunder], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])