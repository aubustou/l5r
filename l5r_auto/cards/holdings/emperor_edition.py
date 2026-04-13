from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Castle, Dojo, Farm, Forest, GeishaHouse, Library, Market, Mine, Port, Retainer, Singular, Stables, Swamp, Temple, Unique
from l5r_auto.legality import CelestialEdition, DiamondEdition, EmperorEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
':bow:: Produce 2 Gold. <br><b>Battle, :bow::</b> Destroy this Holding to destroy a target Terrain.'
Akodos_Grave = Holding(card_id=309, title="Akodo's Grave", gold_cost=2, traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, CelestialEdition, GoldEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'This card will not straighten before your second turn. <br>:bow:: Produce 2 Gold.'
Bamboo_Harvesters = Holding(card_id=679, title='Bamboo Harvesters', gold_cost=0, keywords=[Unique, Forest], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition])
':bow:: Produce 2 Gold. <br><b>Limited:</b> If it is your first turn, put one or more cards in your Provinces at the bottom of your deck, refilling the Provinces face-up.<br><b>Limited:</b> Once per game, put one or more cards in your Provinces at the bottom of your deck, refilling the Provinces face-up.'
Border_Keep = Holding(card_id=1106, title='Border Keep', gold_cost=0, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition])
":bow:: Produce 2 Gold.<br><b>Reaction:</b> When another player's action would target one of your Personalities, destroy this Holding to choose one of your Samurai at the same location. The action targets him instead, if legal."
Chugo_Seido = Holding(card_id=1373, title='Chugo Seido', gold_cost=2, keywords=[Singular, Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Lion Clan player.'
Copper_Mine = Holding(card_id=1497, title='Copper Mine', gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. <br><b>Interrupt:</b> If it is the Action Phase, reduce one of the Honor gains or losses from the action to 0. Destroy this Holding.'
Deeds_and_Words = Holding(card_id=1914, title='Deeds and Words', gold_cost=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Reaction:</b> Before Focus Effects resolve, if your Duelist has a lower duel stat than the Personality facing him, give your Duelist +1 to his duel stat until the duel ends.'
Falling_Rain_Dojo = Holding(card_id=2455, title='Falling Rain Dojo', gold_cost=2, keywords=[Singular, Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. <br><b>Limited:</b> Discard a face-up card from one of your Provinces. Refill the Province with your target discarded <i>(not dead)</i> Personality. Destroy this Holding.'
Family_Library = Holding(card_id=2463, title='Family Library', gold_cost=2, keywords=[Library], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'Your Provinces have +1 strength.'
Fortifications = Holding(card_id=2662, title='Fortifications', gold_cost=0, keywords=[Castle], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Scorpion Clan player.'
Geisha_House = Holding(card_id=2784, title='Geisha House', gold_cost=2, keywords=[GeishaHouse], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Dragon Clan player.'
Gold_Mine = Holding(card_id=2867, title='Gold Mine', gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Political Tireless Open:</b> Choose your performing Courtier and bow him or this Holding to choose another player with an unbowed Personality in play. He may choose to target and bow one of his unbowed Personalities. If he does not choose this, gain 2 Honor.'
Governors_Court = Holding(card_id=2878, title="Governor's Court", gold_cost=2, traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crab Clan player.'
Iron_Mine = Holding(card_id=3808, title='Iron Mine', gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Mantis Clan player.'
Kobune_Port = Holding(card_id=4496, title='Kobune Port', gold_cost=2, keywords=[Port], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, CelestialEdition, GoldEdition, SamuraiEdition, DiamondEdition, ModernEdition])
':bow:: Produce 2 Gold.'
Large_Farm = Holding(card_id=4664, title='Large Farm', gold_cost=1, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, CelestialEdition, GoldEdition, JadeEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Tireless Reaction:</b> When paying for an action, produce 2 Gold which may only pay for that action.'
Luxurious_Silk = Holding(card_id=4787, title='Luxurious Silk', gold_cost=3, traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crane Clan player.'
Marketplace = Holding(card_id=4840, title='Marketplace', gold_cost=2, keywords=[Market], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'After this Holding enters play, put a number of <b>Wealth </b>tokens on it equal to the amount of Gold you paid for it.<br>:bow:: Remove one or more Wealth tokens from this Holding to produce Gold equal to the number of tokens removed.<br><b>Limited, :bow:, :gstar::</b> Put a number of <b>Wealth </b>tokens on this Holding equal to the amount of Gold you paid for this action.'
Moneylender = Holding(card_id=5224, title='Moneylender', gold_cost=0, traits=[], abilities=[], legality=[EmperorEdition, GoldEdition, DiamondEdition, ModernEdition])
'This Holding enters play paying 1 less Gold for each Personality you control.<br>:bow:: Produce 5 Gold.'
Prosperous_Village = Holding(card_id=6086, title='Prosperous Village', gold_cost=6, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold. <br><b>Limited, :bow::</b> Look at the top three cards of your Fate deck. Put them back in any order.'
Public_Records = Holding(card_id=6095, title='Public Records', gold_cost=2, keywords=[Singular], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"This card will not be destroyed; this is not negation.<br>:bow:: Produce 3 Gold.<br><b>Revenge Battle/Open:</b> If you have lost Honor from another player's action during the Action Phase since your last turn ended, choose one to four of your performing Personalities. Give each of them a Force bonus equal to his printed Personal Honor."
Rugashi_Bazaar = Holding(card_id=6396, title='Rugashi Bazaar', gold_cost=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Spider Clan player.'
Shinomen_Marsh = Holding(card_id=6984, title='Shinomen Marsh', gold_cost=2, keywords=[Swamp], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. <br><b>Battle/Open:</b> Straighten a target attachment.'
Shrine_to_Hachiman = Holding(card_id=7223, title='Shrine to Hachiman', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
':bow:: Produce 4 Gold.'
Silk_Works = Holding(card_id=7265, title='Silk Works', gold_cost=5, traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Phoenix Clan player.'
Silver_Mine = Holding(card_id=7266, title='Silver Mine', gold_cost=2, keywords=[Mine], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
':bow:: Produce 1 Gold.'
Small_Farm = Holding(card_id=7303, title='Small Farm', gold_cost=0, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Unicorn Clan player.'
Stables = Holding(card_id=7443, title='Stables', gold_cost=2, keywords=[Stables], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited, :bow::</b> Name "Follower", "Item", or "Spell". Look at the top four cards of your Fate deck. You may show one of those cards that is of the type you named, then put it in your hand.'
Temples_of_Gisei_Toshi = Holding(card_id=7898, title='Temples of Gisei Toshi', gold_cost=2, keywords=[Unique, Temple], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, DiamondEdition, ModernEdition])
':bow:: Produce 2 Gold. <br><b>Limited, :bow:, :g3::</b> Draw a card.'
Traveling_Peddler = Holding(card_id=8729, title='Traveling Peddler', gold_cost=2, keywords=[Singular], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Open, :bow:, :g2::</b> Destroy this Holding to create a 3F/3C/3PH <b>Samurai</b> Personality with your Clan Alignment.'
Venerable_Master = Holding(card_id=9131, title='Venerable Master', gold_cost=2, keywords=[Retainer], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, DiamondEdition, ModernEdition])