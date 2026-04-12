from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Experienced, Forest, Port, Temple, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition
'Bow this card: Produce 2 Gold, or 3 Gold when paying for a Nonhuman.<br><b>Open:</b> Bow this card and target a Nonhuman or Samurai: Straighten him. Straighten one of his attachments if he is Nonhuman.'
Ageless_Shrine = Holding(card_id=166, title='Ageless Shrine', gold_cost=2, keywords=[Forest, Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This card will not straighten before your third turn.<br>:bow:: Produce 2 Gold.<br><b>Limited, :bow::</b> Draw a card. If you now have 6 or more cards in your hand, discard a card.'
Bamboo_Harvesters_Experienced = Holding(card_id=680, title='Bamboo Harvesters', gold_cost=3, keywords=[Unique, Experienced('1'), Forest], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, CelestialEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited:</b> Once per game, put one to three cards in your hand at the bottom of your deck. Draw cards equal to the number you put at the bottom.'
Border_Keep_Experienced = Holding(card_id=1107, title='Border Keep', gold_cost=3, keywords=[Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, CelestialEdition, ModernEdition])
"Your Stronghold's abilities have <b>Tireless</b> <i>(Tireless actions may be taken while bowed.).</i><br>:bow:: Produce 5 Gold."
Colonial_Harbor = Holding(card_id=1431, title='Colonial Harbor', gold_cost=6, keywords=[Port], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, CelestialEdition, ModernEdition])