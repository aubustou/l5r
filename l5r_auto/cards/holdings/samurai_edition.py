from __future__ import annotations
from .common import Holding
from l5r_auto.legality import GoldEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>:bow::</b> Produce 2 Gold. <br><b>Limited, :bow::</b> Gain 1 Honor.'
Kabuki_Theater_Troupe = Holding(card_id=4080, title='Kabuki Theater Troupe', gold_cost=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, GoldEdition, JadeEdition, SamuraiEdition, ModernEdition])