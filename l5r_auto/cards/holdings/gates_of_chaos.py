from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Dojo, Farm, Fortification, Fudo, Jade, Kharmic, Mine, Pearl, PearlBed, Retainer, Singular, Stables, Temple
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"After each player's turn begins, straighten this Holding.<br><b>:bow::</b> Produce 1 Gold."
Abundant_Farmlands = Holding(card_id=10606, title='Abundant Farmlands', gold_cost=1, keywords=[Farm], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Open, :bow::</b> A target Holding's abilities may not be used."
Coastal_Pearl_Bed = Holding(card_id=10615, title='Coastal Pearl Bed', gold_cost=2, keywords=[Pearl, PearlBed], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited:</b> Target a dishonorable Personality. His controller loses 1 Honor.'
Exquisite_Silk_Works = Holding(card_id=10608, title='Exquisite Silk Works', gold_cost=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open, :bow::</b> Give a target Personality and each of his Followers Cavalry.'
Fudoist_Temple = Holding(card_id=10609, title='Fudoist Temple', gold_cost=3, keywords=[Fudo, Temple], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Your Items have +1F.<br><b>:bow::</b> Produce 2 Gold.'
Glassworks = Holding(card_id=10610, title='Glassworks', gold_cost=2, keywords=[Singular, Retainer], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Put a target Terrain in your discard pile into your hand. Destroy this Holding.'
Imperial_Explorers_Dojo = Holding(card_id=10613, title="Imperial Explorer's Dojo", gold_cost=2, keywords=[Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'When this Holding produces Gold, you may give it +1GP <i>(this turn)</i>; if you do, it will not straighten until after your next Action Phase.'
Jade_Mine = Holding(card_id=10614, title='Jade Mine', gold_cost=2, keywords=[Jade, Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i><br><b>:bow::</b> Produce 4 Gold.'
Productive_Mine = Holding(card_id=10607, title='Productive Mine', gold_cost=4, keywords=[Kharmic, Mine], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Courtesy: When this Holding produces Gold, you may give it +1GP <i>(this turn)</i> and lose 2 Honor. <i>(Courtesy traits do not take effect if you went first.)</i>'
Slave_Pits = Holding(card_id=10611, title='Slave Pits', gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Limited, :bow::</b> Give your target Personality Conqueror.'
The_Breeding_Ground = Holding(card_id=10616, title='The Breeding Ground', gold_cost=1, keywords=[Stables], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Fortifications attach, straightened, to the Province from which they entered play.)</i><br><b>Engage, :bow::</b> If you have any units at this battlefield, create a 0F/2C/2PH <b>Samurai &#149; Guard</b> Personality there. Remove him from the game after this battle ends.'
The_Tower_of_Vigilance = Holding(card_id=10612, title='The Tower of Vigilance', gold_cost=0, keywords=[Fortification], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])