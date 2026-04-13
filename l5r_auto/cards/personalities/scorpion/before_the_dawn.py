from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan, SpiritFaction
from l5r_auto.keywords import Assassin, BitterLies, Cavalry, Courtier, Daimyo, Experienced, Goryo, IronFlower, Junshin, Kensai, Loyal, Magistrate, Ninja, Nonhuman, Paragon, Resourceful, Samurai, Spirit, Unique, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle/Open:</b> Target a Weapon in your hand: Attach it to Ebara, paying all costs. Draw a card.'
Bayushi_Ebara = Personality(card_id=763, title='Bayushi Ebara', force=4, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Kensai, BitterLies, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Your provinces have +1 strength while another player controls a dishonorable Personality.'
Bayushi_Shibata = Personality(card_id=879, title='Bayushi Shibata', force=0, chi=3, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[ScorpionClan], keywords=[Courtier, Resourceful], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle/Open:</b> Target your performing Courtier at any location to give Suwabe a Force bonus equal to the Courtier's Chi."
Bayushi_Suwabe = Personality(card_id=901, title='Bayushi Suwabe', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After engaging at Toson's battlefield: Discard a card from the current battlefield's province. If this discarded a Personality, you have the first opportunity to take a Battle action in this battle, which must be performed by Toson."
Shosuro_Toson_Experienced_2 = Personality(card_id=7177, title='Shosuro Toson', force=4, chi=4, personal_honor=1, gold_cost=9, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Experienced('2'), Loyal, Unique, Daimyo, Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card: Bow it.'
Shosuro_Tsuji = Personality(card_id=7179, title='Shosuro Tsuji', force=5, chi=3, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Assassin, Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Battle:</b> Target a Personality with Personal Honor lower than or equal to Komiko's Chi: Bow the Personality. If he is dishonorable, his controller loses 2 Honor."
Soshi_Komiko = Personality(card_id=7355, title='Soshi Komiko', force=4, chi=3, personal_honor=3, gold_cost=7, honor_requirement=0, clan=[ScorpionClan], keywords=[Courtier, IronFlower, Junshin, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target a card without attachments in a unit led by a dishonorable Personality: Destroy the targeted card.'
Wrathful_Dead = Personality(card_id=9391, title='Wrathful Dead', force=3, chi=3, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[ScorpionClan, SpiritFaction], keywords=[Cavalry, Goryo, Nonhuman, Spirit], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])