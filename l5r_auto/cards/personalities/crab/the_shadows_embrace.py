from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Berserker, Courtier, Daimyo, Earth, Elephant, Experienced, Jade, Loyal, Merchant, Nonhuman, Samurai, Scout, Shugenja, Siege, Tactician, TaxCollector, Unique, WitchHunter
from l5r_auto.legality import EmperorEdition, ModernEdition
"Will not attach Items. May not perform Iaijutsu or Political actions. Melee Attacks may not target Chiisai's Followers.<br><b>Fear Battle:</b> Target an enemy Personality with 5 or lower Force: Chiisai charges him. Move him home."
Chiisai = Personality(card_id=9803, title='Chiisai', force=7, chi=2, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[CrabClan], keywords=[Elephant, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Bakari has -4F while he is unopposed.'
Hida_Bakari = Personality(card_id=9804, title='Hida Bakari', force=7, chi=1, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[CrabClan], keywords=[Berserker], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Battle resolution will not bow Personalities with unbowed Followers in Hikazu's army. <i>(Their Followers still bow.)</i>"
Hiruma_Hikazu = Personality(card_id=9805, title='Hiruma Hikazu', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Nikaru uses his Force as his duel stat in duels from other players' cards.<br><b>Battle:</b> Negate the effects of the next Battle action this battle another player takes which targets Nikaru."
Hiruma_Nikaru_Experienced = Personality(card_id=9806, title='Hiruma Nikaru', force=8, chi=2, personal_honor=0, gold_cost=10, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Berserker, Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After your Ranged Attack is targeted: Give it +2 strength. Gain 1 Honor.<br><b>Battle:</b> Target an enemy card with Force lower than this battlefield's province's strength: Bow it. Give the current battlefield's province +2 or -2 strength."
Kaiu_Fumiko = Personality(card_id=9807, title='Kaiu Fumiko', force=5, chi=4, personal_honor=3, gold_cost=10, honor_requirement=4, clan=[CrabClan], keywords=[Tactician, Samurai, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After an action targets Renyu: Reduce any Honor losses from its effects to 0.<br><b>Battle:</b> Target an enemy unit: Its controller may choose to bow it and destroy all Shadowlands cards in it. If he did not choose this, create a province with a base strength of 4 to the left of your leftmost province.'
Kuni_Renyu = Personality(card_id=9808, title='Kuni Renyu', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=None, clan=[CrabClan], keywords=[Loyal, Unique, Daimyo, Earth, Jade, Shugenja, WitchHunter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's Battle action targets one of your Merchants, pay 2 Gold: Either negate its effects on him or make the player lose 2 Honor.<br><b>Battle:</b> Even if Ikke is not at the current battlefield, target your Merchant: Move him home."
Yasuki_Ikke = Personality(card_id=9809, title='Yasuki Ikke', force=2, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, Merchant, TaxCollector], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])