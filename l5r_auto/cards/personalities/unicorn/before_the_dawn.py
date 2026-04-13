from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import AdvisorToTheAmethystChampion, BattleMaiden, Cavalry, Commander, Experienced, GhostGuard, Paragon, Samurai, Scout, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"Kota has +2F while he has a Spell.<br><b>Reaction:</b> After an action targets one of your Personalities at Kota's battlefield: Negate the Personality's movement from the action's effects."
Iuchi_Kota_Experienced = Personality(card_id=3994, title='Iuchi Kota', force=4, chi=4, personal_honor=3, gold_cost=9, honor_requirement=3, clan=[UnicornClan], keywords=[Cavalry, Unique, Experienced('1'), Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Bow Yupadi or one of her Spells, and target a Personality: Give him <b>Naval</b>.'
Iuchi_Yupadi = Personality(card_id=4010, title='Iuchi Yupadi', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, GhostGuard, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target a Follower in your hand: Attach it to Hailung, paying all costs, and paying 4 less Gold if he is defending or if you are a Crab Clan player.'
Moto_Hailung = Personality(card_id=5322, title='Moto Hailung', force=5, chi=3, personal_honor=2, gold_cost=9, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Shinjo_Byung = Personality(card_id=6865, title='Shinjo Byung', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Create a 2F/2C/2PH <b>Unicorn Clan &#149; Samurai &#149; Cavalry &#149; Scout</b> Personality at this battlefield. Remove him from the game after this battle ends.'
Shinjo_Dakho = Personality(card_id=6867, title='Shinjo Dak-ho', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality with lower Personal Honor: Bow him. Gain 2 Honor.'
Utaku_Eunju = Personality(card_id=9061, title='Utaku Eun-ju', force=5, chi=3, personal_honor=4, gold_cost=10, honor_requirement=6, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After a Personality assigns or moves, if he is now opposing Tairu: Draw a card.'
Utaku_Tairu_Experienced = Personality(card_id=9100, title='Utaku Tairu', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Tactician, Unique, AdvisorToTheAmethystChampion, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])