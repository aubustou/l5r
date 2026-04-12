from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Farm, Kolat, Mine, Port, Retainer, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'This card\'s printed ability will not be copied. All players have the ability, "<b>Open, :g6::</b> Destroy a card titled Fortress of Lidless Eyes."<br><b>Kolat Open:</b> Once per game, bow a target Personality. Negate his straightening while this card remains in play.'
Fortress_of_Lidless_Eyes = Holding(card_id=9796, title='Fortress of Lidless Eyes', gold_cost=2, keywords=[Unique, Kolat], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Battle/Open:</b> Destroy this Holding to create a 2F <b>Ashigaru</b> Follower and attach it to your target Personality.'
Humble_Farm = Holding(card_id=9797, title='Humble Farm', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Holding has +1GP when it pays for a single attachment only.'
Platinum_Mine = Holding(card_id=9798, title='Platinum Mine', gold_cost=6, gold_production='5', keywords=[Mine], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
':bow:: Produce 2 Gold, plus 1 Gold for each other Holding you control that is a Market or Port.'
Sheltered_Port = Holding(card_id=9799, title='Sheltered Port', gold_cost=4, keywords=[Port], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you Recruit this Holding, if you control a Courtier or Magistrate, you may dishonor a Personality. <br><b>:bow::</b> Produce 2 Gold.'
SmallTime_Bully = Holding(card_id=9800, title='Small-Time Bully', gold_cost=2, keywords=[Retainer], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Limited, :gstar::</b> Destroy this Holding to search your Dynasty deck for a non-Unique Farm Holding with another title and Recruit it for 2 less Gold; it enters play unbowed.'
Versatile_Farm = Holding(card_id=9801, title='Versatile Farm', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Spells enter play for 1 less Gold.'
Whispering_Archive = Holding(card_id=9802, title='Whispering Archive', gold_cost=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])