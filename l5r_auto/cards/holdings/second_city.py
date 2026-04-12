from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Dojo, Farm, Ninja, Retainer, Temple
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
':bow:: Produce 2 Gold.<br><b>Reaction:</b> After a Ranged Attack is targeted, give it +1 strength.'
Archery_Range = Holding(card_id=430, title='Archery Range', gold_cost=2, keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 3 Gold, or 4 Gold when paying for a Ninja card which may only pay for that card.<br><b>Ninja Tireless Reaction, :bow::</b> After an action targets your Personality, remove <b>Ninja </b>and<b> Shadowlands </b>from him until the action ends.'
Red_Crane_Dojo = Holding(card_id=6219, title='Red Crane Dojo', gold_cost=4, keywords=[Dojo, Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 3 Gold.'
Remote_Village = Holding(card_id=6258, title='Remote Village', gold_cost=3, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>:bow::</b> Produce 5 Gold. <br><b>Political Limited, :bow::</b> If you control a Courtier or Magistrate, dishonor a target Personality.'
Slanderer = Holding(card_id=7291, title='Slanderer', gold_cost=6, keywords=[Retainer], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited:</b> Bow your performing Shugenja to gain 1 Honor.'
Temple_of_Hotei = Holding(card_id=7875, title='Temple of Hotei', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Open, :bow::</b> Target a Ring in play or in your discard pile. If the Ring is in play, straighten it. Otherwise, put it into your hand and destroy this Holding.'
Tranquil_Garden = Holding(card_id=8721, title='Tranquil Garden', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])