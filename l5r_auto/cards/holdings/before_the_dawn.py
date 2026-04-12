from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Castle, Farm, Kolat, Market, Port, Retainer, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Political Open:</b> If another player's action has caused you an Honor loss this turn, give your target Personality a +1F Revenge token."
Beautiful_Host = Holding(card_id=943, title='Beautiful Host', gold_cost=2, keywords=[Retainer], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, CelestialEdition, OnyxEdition, ModernEdition])
":bow:: Produce 2 Gold.<br><b>Siege Absent Battle, :bow::</b> Increase the current battlefield's Province's strength by 2."
Indomitable_Home = Holding(card_id=3737, title='Indomitable Home', gold_cost=2, keywords=[Castle], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold. <br><b>Reaction:</b> When paying a Gold Cost, produce 1 Gold. <i>(This can be used together with bowing this card to produce Gold.)</i>'
Seaside_Bazaar = Holding(card_id=6529, title='Seaside Bazaar', gold_cost=4, keywords=[Farm, Market, Port], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Kolat Open:</b> Target another player's Holding with a printed Gold Cost from 1 to 4. This Holding copies one of its printed abilities that does not itself copy abilities, one of its Gold-producing traits, or its Gold Production stat."
Stolen_Merchandise = Holding(card_id=7494, title='Stolen Merchandise', gold_cost=2, keywords=[Unique, Kolat, Retainer], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])