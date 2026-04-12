from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Castle, Dojo, Experienced, Farm, Forest, Kharmic, Market, Oracle, Retainer, SakeHouse, Temple, Unique, Void, Winter
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'You may include up to five copies of this card in your deck.<br>After this Holding enters play, if you have a Clan Alignment, lose 3 Honor.<br>:bow:: Produce 2 Gold, or 3 Gold if you are paying for a Ronin; if the latter, it may only pay for that Ronin.'
Bandits_Sanctuary = Holding(card_id=10187, title="Bandit's Sanctuary", gold_cost=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Enters play for 1 less Gold if you are a Lion Clan player.<br>:bow:: Produce 5 Gold.<br><b>Limited, :bow::</b> Create a 1F <b>Ashigaru </b> Follower and attach it to your target Personality.'
Colonial_Farm = Holding(card_id=10231, title='Colonial Farm', gold_cost=6, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"This card will not be destroyed and other players will not lose Honor from your Spells; these are not negation.<br>:bow:: Produce 2 Gold.<br><b>Political Limited, :bow::</b> Target another player's dishonorable Personality. His controller loses Honor equal to his printed Personal Honor, or 3, whichever is lower. You may not declare an attack this turn."
Den_of_Iniquity = Holding(card_id=1950, title='Den of Iniquity', gold_cost=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: When another Holding produces Gold to pay for a Nonhuman, produce 1 Gold which may only pay for that card.'
EverWinter_Copse = Holding(card_id=2391, title='Ever-Winter Copse', gold_cost=0, keywords=[Forest, Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Battle, :bow::</b> Give each of your Followers at this battle +1F.'
Family_Dojo = Holding(card_id=10573, title='Family Dojo', gold_cost=2, keywords=[Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
':bow:: Produce 5 Gold.<br><b>Limited:</b> If another player has higher Family Honor than you, gain 1 Honor.'
Forgotten_Outpost = Holding(card_id=2658, title='Forgotten Outpost', gold_cost=6, keywords=[Castle, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle, :bow::</b> Give a target Personality or Follower +2F.'
Generals_Hatamoto = Holding(card_id=10572, title="General's Hatamoto", gold_cost=1, keywords=[Retainer], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'You may Equip Weapons from under this Holding as a <b>Battle/Limited</b> action.<br><b>Limited:</b> Put a Weapon in your hand under this Holding <i>(face-down)</i>.'
Hidden_Weapons = Holding(card_id=10574, title='Hidden Weapons', gold_cost=0, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. <br><b>Open, :bow::</b> Straighten your target Courtier.'
Jiramus_Court = Holding(card_id=10189, title="Jiramu's Court", gold_cost=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
':bow:: Produce 3 Gold, or 4 Gold if paying for an attachment which may only pay for that card.<br><b>Open:</b> Choose your two performing Personalities and transfer a target attachment on one of them to the other.'
Jungle_Stockade = Holding(card_id=4066, title='Jungle Stockade', gold_cost=4, keywords=[Dojo, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This card cannot be destroyed.<br><b>Limited, :bow::</b> The next two cards in provinces you refill <i>(this turn)</i> may be refilled face-up.<br><b>Limited, :bow::</b> Draw a card.'
Oracle_of_the_Void_Experienced = Holding(card_id=10408, title='Oracle of the Void', gold_cost=6, keywords=[Unique, Experienced('1'), Oracle, Retainer, Void], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Your Stronghold produces one more Gold, to a maximum of 5, when paying for a non-Personality card which may only pay for that card.<br>:bow: Produce 2 Gold.'
Plantation = Holding(card_id=9953, title='Plantation', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open, :bow::</b> Give each of your Sake tokens +1F.'
Public_Room = Holding(card_id=6097, title='Public Room', gold_cost=0, keywords=[SakeHouse], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Tireless Battle:</b> Give your target Personality +2F.'
Retired_Sensei = Holding(card_id=9955, title='Retired Sensei', gold_cost=3, keywords=[Retainer], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Other players' actions will not discard cards from your hand.<br>:bow:: Produce 2 Gold."
Sacred_Temples = Holding(card_id=10409, title='Sacred Temples', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited:</b> Destroy this Holding to draw a card.'
Second_City_Dojo = Holding(card_id=6539, title='Second City Dojo', gold_cost=2, keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>:bow::</b> Bow your target unbowed Courtier or Artisan. Produce Gold equal to his Chi.'
The_Amethyst_Court = Holding(card_id=10752, title='The Amethyst Court', gold_cost=3, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Straighten your target Personality.'
The_Emerald_Dojo = Holding(card_id=10753, title='The Emerald Dojo', gold_cost=3, keywords=[Unique, Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Bow your target unbowed Personality. Bow a target dishonorable Personality.'
The_Ivory_Dojo = Holding(card_id=10754, title='The Ivory Dojo', gold_cost=3, keywords=[Unique, Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Battle, :bow::</b> Straighten your target Spell. You may use its abilities a second time.'
The_Jade_Temple = Holding(card_id=10755, title='The Jade Temple', gold_cost=3, keywords=[Unique, Temple], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Permanently give your target Samurai Shadowlands. Give him three +1F tokens. Destroy this Holding. Lose 4 Honor.'
The_Obsidian_Dueling_Grounds = Holding(card_id=10756, title='The Obsidian Dueling Grounds', gold_cost=3, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Destroy your target Shugenja. Create a 5F/2C/0PH <b>Nonhuman &#149; Oni &#149; Shadowlands</b> Personality. Destroy this Holding. Lose 4 Honor.'
The_Onyx_Dueling_Circle = Holding(card_id=10757, title='The Onyx Dueling Circle', gold_cost=3, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Political Limited, :bow::</b> Bow your target unbowed Magistrate Personality. Dishonor a target Personality.'
The_Ruby_Dojo = Holding(card_id=10758, title='The Ruby Dojo', gold_cost=3, keywords=[Unique, Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Give a +1F/+1C <b>Training </b>token to a target Personality with no printed abilities and no Training tokens.'
The_Topaz_Dojo = Holding(card_id=10759, title='The Topaz Dojo', gold_cost=3, keywords=[Unique, Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Political Limited, :bow::</b> Bow your target unbowed Personality. You, or any player if the Personality is an Artisan, gain or lose 1 Honor.'
The_Turquoise_Court = Holding(card_id=10760, title='The Turquoise Court', gold_cost=3, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
Traveling_Market = Holding(card_id=10571, title='Traveling Market', gold_cost=3, keywords=[Kharmic, Market], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])