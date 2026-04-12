from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Inexperienced, Temple
from l5r_auto.legality import EmperorEdition, ModernEdition
':bow:: When paying for a Spell or Shugenja, produce 5 Gold which may only pay for that card.'
The_Sacred_Temple_of_the_Phoenix_Inexperienced = Stronghold(card_id=10256, title='The Sacred Temple of the Phoenix', gold_production='3', starting_family_honor=6, province_strength=5, clan=[PhoenixClan], keywords=[Inexperienced, Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])