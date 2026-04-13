from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Cavalry, Courtier, Duelist, Experienced, Imperial, ImperialExplorer, IronCrane, Jade, JadeChampion, Magistrate, Overconfident, Samurai, Scout, Shugenja, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'Melee and Ranged Attacks targeting Akahiko have -4 strength.<br><b>Battle:</b> Target an enemy Personality: Move him and Akahiko home. Gain 1 Honor.'
Asahina_Akahiko = Personality(card_id=10278, title='Asahina Akahiko', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=2, clan=[CraneClan], keywords=[Cavalry, Air, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Even if Nanae is bowed, target a Personality: You may straighten him. You may give him -4F. Bow him if he is Shadowlands.'
Asahina_Nanae_Experienced = Personality(card_id=10279, title='Asahina Nanae', force=2, chi=4, personal_honor=4, gold_cost=8, honor_requirement=9, clan=[CraneClan], keywords=[Unique, Air, Experienced('1'), Jade, JadeChampion, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality or Follower: Move Ibara to oppose it. If she now opposes it, give it -3F and, if it is Mantis Clan, bow it.'
Daidoji_Ibara = Personality(card_id=10280, title='Daidoji Ibara', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=5, clan=[CraneClan], keywords=[IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target another player's Mirumoto Kyoshiro: Iza duels him. Destroy the duel's loser."
Doji_Iza = Personality(card_id=10281, title='Doji Iza', force=2, chi=3, personal_honor=4, gold_cost=6, honor_requirement=6, clan=[CraneClan], keywords=[Duelist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'During a duel involving Kazuo, the other player must focus from his hand at his first opportunity<i>(if able)</i>.<br>After your End Phase begins, if Kazuo won a duel, or you have gained 4 or more Honor, this turn: Look at the top 3 cards of a Fate deck. Put them back in any order.'
Doji_Kazuo_Experienced = Personality(card_id=10282, title='Doji Kazuo', force=2, chi=5, personal_honor=4, gold_cost=9, honor_requirement=6, clan=[CraneClan], keywords=[Duelist, Overconfident, Unique, Courtier, Experienced('1'), Imperial, ImperialExplorer, Magistrate, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Political Open:</b> Target a Personality: While he is at the current battlefield <i>(later this turn)</i>, you may take a Battle action even if you control no units there. After that action ends, end this action's effects on him."
Doji_Tatsuzo = Personality(card_id=10283, title='Doji Tatsuzo', force=1, chi=3, personal_honor=4, gold_cost=7, honor_requirement=5, clan=[CraneClan], keywords=[Courtier], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])