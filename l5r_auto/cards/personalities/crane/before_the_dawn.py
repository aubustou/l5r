from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Artisan, Cavalry, Courtier, Duelist, Experienced, IronCrane, Kenku, Magistrate, Nonhuman, Samurai, Scout, Shugenja, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Open:</b> Target an Air Personality: Straighten him.'
Asahina_Nanae = Personality(card_id=507, title='Asahina Nanae', force=2, chi=4, personal_honor=4, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Air, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow Masafuni unless you have Reconnaissance, and target a Personality: Move him home.'
Daidoji_Masafuni = Personality(card_id=1653, title='Daidoji Masafuni', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=4, clan=[CraneClan], keywords=[IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Target a Personality with lower Personal Honor than Shigeyuki's Chi: Shigeyuki challenges him. He may refuse; if he does, move him home. Both Personalities use their Personal Honor as their duel stat. Bow the duel's loser's unit."
Doji_Shigeyuki = Personality(card_id=2152, title='Doji Shigeyuki', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=5, clan=[CraneClan], keywords=[Duelist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Open:</b> Target a Personality: He may not perform actions until the current phase ends.'
Kakita_Munemori_Experienced = Personality(card_id=4203, title='Kakita Munemori', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[CraneClan], keywords=[Unique, Courtier, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Your Stronghold's abilities have <b>Tireless</b>.<br><b>Favor Political Open:</b> Discard the Imperial Favor to give each of your Provinces +2 strength."
Kakita_Nara = Personality(card_id=4206, title='Kakita Nara', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Courtier], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Remove a card in your Fate discard pile from the game and target your Personality: Create a +1F/+0C <b>Weapon</b> Item and attach it to him.'
Kakita_Yasunori = Personality(card_id=4240, title='Kakita Yasunori', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[CraneClan], keywords=[Artisan], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Takayuki = Personality(card_id=7742, title='Takayuki', force=4, chi=4, personal_honor=4, gold_cost=8, honor_requirement=6, clan=[CraneClan], keywords=[Cavalry, Duelist, Kenku, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])