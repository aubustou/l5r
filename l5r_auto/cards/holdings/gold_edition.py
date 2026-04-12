from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Dojo, Fortification, Jade
from l5r_auto.legality import EmperorEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
':bow:: When paying for an action that Equips or creates a Follower, produce 6 Gold which may only pay for one action.'
Bushi_Dojo = Holding(card_id=1190, title='Bushi Dojo', gold_cost=3, keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>:bow::</b> Produce 3 Gold. <br><b>:bow::</b> Produce 5 Gold, which can only pay for a single Jade card.'
Jade_Works = Holding(card_id=4036, title='Jade Works', gold_cost=3, keywords=[Jade], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
'<i>(Fortifications attach to the Province from which they entered play.)</i><br>Enters play unbowed. <br><b>Limited, :bow::</b> Gain 2 Honor.'
Poorly_Placed_Garden = Holding(card_id=6021, title='Poorly Placed Garden', gold_cost=5, keywords=[Fortification], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, JadeEdition, ModernEdition])