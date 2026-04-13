from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Acrobat, Courtier, Experienced, Loyal, Magistrate, Ninja, Nonhuman, Paragon, Samurai, TamamoNoMae, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Open:</b> If it is another player's turn, target one of his Personalities: Before this phase ends, straighten him. Before this turn ends, if the Personality was not assigned to attack this turn, dishonor him and his controller loses Honor equal to his base Personal Honor."
Bayushi_Misaki = Personality(card_id=9842, title='Bayushi Misaki', force=2, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[ScorpionClan], keywords=[Courtier, Nonhuman, TamamoNoMae], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Enters play paying 2 less Gold if you control a Courtier.'
Bayushi_Tarou = Personality(card_id=9843, title='Bayushi Tarou', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[ScorpionClan], keywords=[Loyal, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Bow him. If you control a Courtier, negate the effects of the next action the target performs <i>(this turn)</i>.'
Bayushi_Waru_Experienced = Personality(card_id=9844, title='Bayushi Waru', force=5, chi=3, personal_honor=3, gold_cost=9, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Unique, Experienced('1'), Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Move Keirei from the current battlefield to a different battlefield. You may target and give a Personality at Keirei's new or previous location two -1F/-1C <b>Poison</b> tokens."
Shosuro_Keirei_Experienced = Personality(card_id=9845, title='Shosuro Keirei', force=5, chi=3, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Experienced('Bayushi Keirei'), Unique, Acrobat, Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Move him home.'
Shosuro_Nobu = Personality(card_id=9846, title='Shosuro Nobu', force=5, chi=3, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Political Reaction:</b> After Ryoken enters play, target a Personality: Dishonor him.<br><b>Political Reaction:</b> After a battle resolves, if Ryoken was at its battlefield during its resolution in which you destroyed a province or army: The enemy leader loses 2 Honor.'
Shosuro_Ryoken = Personality(card_id=9847, title='Shosuro Ryoken', force=3, chi=2, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[ScorpionClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])