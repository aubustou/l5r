from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Cavalry, Courtier, Daimyo, Duelist, IronCrane, Loyal, Magistrate, Naval, Overconfident, Samurai, Scout, Shugenja, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Reaction:</b> After an action on your Air Spell resolves: Gain 1 Honor.'
Asahina_Akikusa = Personality(card_id=10046, title='Asahina Akikusa', force=3, chi=4, personal_honor=4, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Loyal, Unique, Air, Daimyo, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<i>(Each other player may draw a card after an Overconfident card enters or leaves play.)</i> <br>Other players' maximum hand sizes are increased by 1."
Asahina_Tsugio = Personality(card_id=10047, title='Asahina Tsugio', force=0, chi=3, personal_honor=3, gold_cost=2, honor_requirement=6, clan=[CraneClan], keywords=[Overconfident, Air, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow Kitahime unless you have Reconnaissance: Ranged 4 Attack.'
Daidoji_Kitahime = Personality(card_id=10048, title='Daidoji Kitahime', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=5, clan=[CraneClan], keywords=[Cavalry, IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target an enemy Personality: Mitsuru duels him. Bow the duel's loser."
Doji_Mitsuru = Personality(card_id=10049, title='Doji Mitsuru', force=3, chi=4, personal_honor=3, gold_cost=8, honor_requirement=2, clan=[CraneClan], keywords=[Duelist, Naval, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Yuka performs a Political action: Give her +3C until it ends.'
Doji_Yuka = Personality(card_id=10050, title='Doji Yuka', force=1, chi=3, personal_honor=4, gold_cost=5, honor_requirement=10, clan=[CraneClan], keywords=[Courtier], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'You may take the Proclaim Reaction to Yusugi entering play even if you have already used the Proclaim ability once this turn.'
Kakita_Yusugi = Personality(card_id=10051, title='Kakita Yusugi', force=2, chi=3, personal_honor=2, gold_cost=4, honor_requirement=6, clan=[CraneClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])