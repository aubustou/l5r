from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, Dog, Experienced, Loyal, Nonhuman, Paragon, Samurai, Shugenja, Tactician, TheKhan, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Battle:</b> Bow one of Haruma's Spells: Give him +2F. Ranged 4 Attack."
Iuchi_Haruma = Personality(card_id=9859, title='Iuchi Haruma', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will not attach cards.<br><b>Battle:</b> Target an enemy Follower or Personality without Followers: Destroy it.'
Longtooth_Experienced = Personality(card_id=9860, title='Longtooth', force=4, chi=2, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Experienced('Unicorn War Dogs'), Unique, Dog, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Follower. Melee Attack with strength equal to its Force.'
Moto_Morio = Personality(card_id=9861, title='Moto Morio', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Tactical action Jong-Ho performed resolves, target a card opposing him with lower Force: Bow it.'
Shinjo_JongHo = Personality(card_id=9862, title='Shinjo Jong-Ho', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a Follower in your discard pile: Put it into your hand.<br><b>Tactical Battle:</b> Target an enemy card without attachments: Destroy it. Remove it from the game if it is Dragon Clan. You may discard a Follower <i>(from your hand)</i>; if you did, draw a card.'
Shinjo_MinHee = Personality(card_id=9863, title='Shinjo Min-Hee', force=6, chi=4, personal_honor=3, gold_cost=12, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, Loyal, Tactician, Unique, Commander, Samurai, TheKhan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Utaku_SungKi = Personality(card_id=9864, title='Utaku Sung-Ki', force=2, chi=1, personal_honor=3, gold_cost=3, honor_requirement=10, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])