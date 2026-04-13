from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, Experienced, Paragon, Samurai, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle:</b> Choose a Personality in a discard pile, remove him from the game, and target an enemy Personality: Move him home. Bow him if the Personality you chose was dead.'
Iuchi_Abodan = Personality(card_id=3974, title='Iuchi Abodan', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Followers in Xiao's army have +1F.<br><b>Battle:</b> Destroy a target enemy card without attachments."
Moto_Xiao_Experienced = Personality(card_id=5395, title='Moto Xiao', force=6, chi=4, personal_honor=3, gold_cost=10, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Unique, Commander, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Even if Junpei is not at the current battlefield, target an enemy card without attachments: Bow it. If it is a Personality, negate his next movement.'
Shinjo_Junpei = Personality(card_id=6900, title='Shinjo Junpei', force=3, chi=4, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[UnicornClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Negate Ji-Yun's dishonoring from other players' cards' effects."
Utaku_JiYun = Personality(card_id=9071, title='Utaku Ji-Yun', force=5, chi=3, personal_honor=4, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])