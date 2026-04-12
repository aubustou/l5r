from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Castle, Farm, Temple, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
":bow:: Produce 2 Gold, or 3 Gold if you control a Tactician.<br><b>Limited, :bow::</b> Bow your performing Lion Clan Tactician to lower a target a Province's strength to 0."
Shrine_to_Nimuro = Holding(card_id=7227, title='Shrine to Nimuro', gold_cost=3, keywords=[Unique, Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 3 Gold, or 4 Gold if paying for a card with a printed Gold Cost of 9 or more which may only pay for that card.'
Staging_Grounds = Holding(card_id=7444, title='Staging Grounds', gold_cost=4, keywords=[Castle], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited:</b> If you have fewer Provinces than each other player, or exactly one Province, give your performing Siege Personality <b>Conqueror</b>.'
Surveillance_Outpost = Holding(card_id=7671, title='Surveillance Outpost', gold_cost=2, keywords=[Castle], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After the first time each turn you bow this Holding, gain 1 Honor.'
Temple_Fortress = Holding(card_id=7869, title='Temple Fortress', gold_cost=4, keywords=[Castle, Temple], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>:bow::</b> Produce 5 Gold. <br><b>Open:</b> Give your target Monk or Shugenja <b>Air</b>, <b>Earth</b>, <b>Fire</b>, or <b>Water</b>.'
Temple_to_the_Elements = Holding(card_id=7897, title='Temple to the Elements', gold_cost=6, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Battle, :bow::</b> Give each of your Ashigaru cards at the current battlefield +1F.'
Terraced_Farm = Holding(card_id=7915, title='Terraced Farm', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])