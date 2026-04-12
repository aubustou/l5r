from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Fire, Shugenja
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'Hikarou has +1F for each of his Fire Spells.'
Isawa_Hikarou = Personality(card_id=10580, title='Isawa Hikarou', force=2, chi=3, personal_honor=2, gold_cost=5, honor_requirement=2, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])