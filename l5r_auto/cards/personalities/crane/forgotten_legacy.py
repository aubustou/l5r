from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Artisan, Courtier, Duelist, Experienced, FirstMagistrate, IronCrane, Loyal, Magistrate, Samurai, Scout, Shugenja, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Open:</b> Bow Shigemitsu or one of his Spells: Give each of your provinces +1 strength. If it is not your turn, before it ends, if none of your provinces were destroyed this turn, gain 1 Honor.'
Asahina_Shigemitsu = Personality(card_id=515, title='Asahina Shigemitsu', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Air, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target a Personality opposing Takichi at the current battlefield: Move the Personality and Takichi to the same adjacent unresolved battlefield.'
Daidoji_Takichi = Personality(card_id=1679, title='Daidoji Takichi', force=4, chi=3, personal_honor=3, gold_cost=7, honor_requirement=0, clan=[CraneClan], keywords=[IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Open:</b> Target a Personality: Choose one of his abilities; it may not be used.<br><b>Battle:</b> Target an enemy Personality: Hakuseki issues him an unrefusable challenge. The controller of the duel's winner gains 2 Honor. Bow the duel's loser, and destroy him if he is dishonorable."
Doji_Hakuseki_Experienced_2 = Personality(card_id=2082, title='Doji Hakuseki', force=4, chi=5, personal_honor=4, gold_cost=10, honor_requirement=6, clan=[CraneClan], keywords=[Duelist, Experienced('2'), Loyal, Unique, FirstMagistrate, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Favor Political Open:</b> Discard the Imperial Favor to target a Personality or Holding. Choose one of its abilities; it may not be used.'
Doji_Rengetsu = Personality(card_id=2142, title='Doji Rengetsu', force=0, chi=4, personal_honor=4, gold_cost=6, honor_requirement=6, clan=[CraneClan], keywords=[Artisan, Courtier], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])