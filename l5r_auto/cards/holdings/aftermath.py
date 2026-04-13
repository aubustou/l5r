from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Destined, Dojo, Farm, Market
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>:bow::</b> Produce 2 Gold.<br><b>:bow::</b> When paying for an Item, it enters play for 3 less Gold.'
Exotic_Market = Holding(card_id=10824, title='Exotic Market', gold_cost=2, keywords=[Market], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br><b>:bow::</b> Produce 3 Gold.'
House_of_Prophecy = Holding(card_id=10825, title='House of Prophecy', gold_cost=4, keywords=[Destined], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Interrupt:</b> After you Recruit this Holding from a Province, search your Dynasty deck for a non-Unique, Gold-producing Holding with a printed Gold Cost of 1 and refill the Province face-up with it.<br><b>:bow::</b> Produce 3 Gold.'
Jade_Pearl_Inn = Holding(card_id=10826, title='Jade Pearl Inn', gold_cost=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"Before another, non-Spider Clan player loses Honor from a card he owns, increase the loss by an amount equal to half his Starting Family Honor, rounded down <i>(this doesn't allow them to ignore Honor Requirements)</i>."
Nexus_of_Lies = Holding(card_id=10827, title='Nexus of Lies', gold_cost=4, gold_production='4', traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"This Holding has -1GP while your Stronghold's Gold Production is 4 or greater."
Suana_Dojo = Holding(card_id=10828, title='Suana Dojo', gold_cost=3, keywords=[Dojo], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Your Ashigaru Personalities and Followers have +1F while opposed.<br><b>:bow::</b> Produce 2 Gold.'
WellDefended_Farm = Holding(card_id=10829, title='Well-Defended Farm', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open, :bow::</b> A target Holding's abilities may not be used."
Yukihimes_Hot_Springs = Holding(card_id=10830, title="Yukihime's Hot Springs", gold_cost=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])