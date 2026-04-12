from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Inexperienced, Unique, Winter
from l5r_auto.legality import EmperorEdition
':bow:: Produce 2 Gold. <br><b>Limited:</b> If it is your first turn, put one or more cards in your Provinces at the bottom of your deck, refilling the Provinces face-up.'
Border_Keep_Inexperienced = Holding(card_id=10240, title='Border Keep', gold_cost=0, keywords=[Unique, Inexperienced, Winter], traits=[], abilities=[], legality=[EmperorEdition])