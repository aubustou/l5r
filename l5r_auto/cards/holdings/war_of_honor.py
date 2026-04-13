from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Temple, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>:bow::</b> Produce 2 Gold. <br><b>:bow::</b> When paying for a Monk, he enters play for 3 less Gold.'
Temple_of_Harmony = Holding(card_id=7874, title='Temple of Harmony', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Open:</b> Destroy this Holding to search your Fate deck for a Ring. Show it and put it in your hand. Shuffle your Fate deck.'
The_Seekers_Temple = Holding(card_id=8308, title="The Seekers' Temple", gold_cost=2, keywords=[Unique, Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])