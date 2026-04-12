from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Castle, Dojo, Imperial, Mine, Port, Retainer, SakeHouse, SakeWorks, Temple, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
':bow:: Produce 1 Gold.<br><b>Limited, :bow::</b> Give a target Personality a +1F <b>Sake </b>token.'
Blue_Tanuki_Bar = Holding(card_id=1081, title='Blue Tanuki Bar', gold_cost=1, keywords=[SakeWorks], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>:bow::</b> Produce 3 Gold. <br><b>Battle, :bow::</b> Give your target Personality +2F.'
Heavy_Infantry_Dojo = Holding(card_id=3044, title='Heavy Infantry Dojo', gold_cost=4, keywords=[Dojo], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. <br><b>Limited, :bow::</b> Give a target Personality a +1F <b>Sake </b>token. Remove it after your next turn begins.'
Humble_House = Holding(card_id=3510, title='Humble House', gold_cost=2, keywords=[SakeHouse], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold, or 3 Gold if paying for a Magistrate which may only pay for that card.<br><b>Reaction:</b> After you announce a non-Iaijutsu action, choose your performing Magistrate to give him +1C until the action ends.'
Magistrates_Stipend = Holding(card_id=4795, title="Magistrate's Stipend", gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Your Provinces have +1 strength. <br><b>:bow::</b> Produce 5 Gold.'
Merchant_Atoll = Holding(card_id=5027, title='Merchant Atoll', gold_cost=6, keywords=[Castle, Port], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 3 Gold.<br><b>Reaction, :bow::</b> After engaging at a battlefield where you control one or more units, create a 2F/2C/2PH <b>Ronin &#149; Samurai</b> Personality there. Remove him from the game when this turn ends.'
Recruitment_Officer = Holding(card_id=6218, title='Recruitment Officer', gold_cost=4, keywords=[Retainer], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold.<br>After one of your Celestials is revealed in a Province, you may choose one of your Celestials in play. If you do, it is not discarded because of the other Celestial entering play.'
Shrine_to_the_Heavens = Holding(card_id=7229, title='Shrine to the Heavens', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"This Holding does not count towards your minimum deck size.<br><b>Reaction:</b> After another player's action targets one of your cards, remove this card from the game and then tear it in half to negate the target's destruction from the action's effects."
Stone_of_Remembrance = Holding(card_id=7501, title='Stone of Remembrance', gold_cost=0, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This Holding enters play for 1 less Gold if you are a Mantis Clan player.<br>:bow:: Produce 1 Gold, plus 1 additional Gold for each non-Unique Holding you control.'
The_Imperial_Treasury = Holding(card_id=8150, title='The Imperial Treasury', gold_cost=4, keywords=[Unique, Imperial], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])