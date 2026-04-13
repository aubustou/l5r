from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, DemonSlayer, Experienced, Imperial, MoonBlessed, Paragon, Sacrosanct, Samurai, Scout, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"Followers in this unit have <b>Cavalry</b>.<br><b>Limited:</b> Target a Follower in any player's discard pile: Attach it to Jun-Ni, paying all costs."
Moto_JunNi = Personality(card_id=5337, title='Moto Jun-Ni', force=4, chi=2, personal_honor=2, gold_cost=8, honor_requirement=2, clan=[UnicornClan], keywords=[Cavalry, Commander, DemonSlayer, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> If there is a dead Personality in any player's discard pile: Ranged 5 Attack."
Moto_MingGwok = Personality(card_id=5351, title='Moto Ming-Gwok', force=4, chi=4, personal_honor=1, gold_cost=9, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, MoonBlessed, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Move him home. This movement will not be negated if you have Reconnaissance.'
Shinjo_Kinto = Personality(card_id=6906, title='Shinjo Kinto', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Shinjo_Sanenari = Personality(card_id=6931, title='Shinjo Sanenari', force=2, chi=3, personal_honor=2, gold_cost=5, honor_requirement=4, clan=[UnicornClan], keywords=[Tactician, Sacrosanct, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After the resolution of an action that gave a Force penalty to an enemy card at Liu-Xeung's battlefield: Give Liu-Xeung +1F.<br><b>Battle:</b> Target an enemy Personality with lower Personal Honor: Move him home. Gain 1 Honor."
Utaku_LiuXeung_Experienced = Personality(card_id=9085, title='Utaku Liu-Xeung', force=4, chi=3, personal_honor=4, gold_cost=9, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Unique, BattleMaiden, Experienced('1'), Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Target an enemy Personality or Follower: You may move Mai to the current battlefield. If she is now there, give the targeted card a Force penalty equal to Mai's Personal Honor."
Utaku_Mai = Personality(card_id=9086, title='Utaku Mai', force=4, chi=4, personal_honor=4, gold_cost=8, honor_requirement=5, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Imperial, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])