from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Berserker, Courtier, Daimyo, Earth, Experienced, Hero, Imperial, Jade, Loyal, Merchant, Samurai, Scout, Shugenja, Siege, Tactician, Unique, WitchHunter, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
Hida_Chiyurei = Personality(card_id=10272, title='Hida Chiyurei', force=2, chi=1, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[CrabClan], keywords=[Tactician, Berserker], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Before the first time each battle any of Ikeuchi's Followers are destroyed by another player's card's effect: If you have Reconnaissance, negate the destruction of one such Follower."
Hiruma_Ikeuchi = Personality(card_id=10273, title='Hiruma Ikeuchi', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[CrabClan], keywords=[Imperial, Samurai, Scout, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While Nagai is defending, he has <b>Elite </b><i>(Elite cards contribute Force even if bowed)</i>.'
Kaiu_Nagai = Personality(card_id=10274, title='Kaiu Nagai', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=3, clan=[CrabClan], keywords=[Tactician, Samurai, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your provinces have +2 strength.<br>Your other Personalities with a base Gold Cost of 5 or higher enter play paying 2 less Gold.'
Kuni_Renyu_Experienced = Personality(card_id=10275, title='Kuni Renyu', force=5, chi=4, personal_honor=3, gold_cost=10, honor_requirement=None, clan=[CrabClan], keywords=[Loyal, Unique, Daimyo, Earth, Experienced('1'), Jade, Shugenja, WitchHunter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card: Bow it. Destroy it if it is Shadowlands.'
Kuni_Shinoda_Experienced = Personality(card_id=10276, title='Kuni Shinoda', force=3, chi=4, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[CrabClan], keywords=[Tactician, Unique, Earth, Experienced('1'), Hero, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Bow Daito or pay 4 Gold, and target a Personality: Daito bribes him. Negate the target's straightening until after the next Straighten Phase ends."
Yasuki_Daito = Personality(card_id=10277, title='Yasuki Daito', force=2, chi=4, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])