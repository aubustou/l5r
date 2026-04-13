from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, Experienced, Loyal, MasterOfTheSwiftWaves, Paragon, Samurai, Sensei, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
Iuchi_Yuri = Personality(card_id=4011, title='Iuchi Yuri', force=6, chi=5, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, MasterOfTheSwiftWaves, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Even if Isul is at home, target a Personality: Bow or straighten him.'
Moto_Isul = Personality(card_id=5332, title='Moto Isul', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Water Reaction:</b> When paying for a Spell Equipping to Rani, remove a dead Personality in your discard pile from the game to reduce the Spell's Gold Cost by the Personality's Chi.<br><b>Water Tireless Battle:</b> Straighten Rani. You may move her home."
Moto_Rani_Experienced = Personality(card_id=5361, title='Moto Rani', force=4, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Unique, DeathPriest, Experienced('1'), Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Hayan enters play: Discard all your other Sensei Personalities.<br>After engaging: Once per turn, you may assign your <i>(unbowed)</i> Unicorn Clan Personality in your home to the current battlefield.'
Shinjo_Hayan = Personality(card_id=6883, title='Shinjo Hayan', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Loyal, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Tactical Battle:</b> Even if Junpei is at home, choose your performing unbowed Personality: Melee 4 Attack.'
Shinjo_Junpei_Experienced = Personality(card_id=6901, title='Shinjo Junpei', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[UnicornClan], keywords=[Tactician, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Personality, and target your Follower at any location: Transfer it to the Personality. Straighten the Follower if the Personality is opposed or Spider Clan.'
Shinjo_Sarang = Personality(card_id=6934, title='Shinjo Sarang', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"While Lishan is attacking, she has +1F and +1PH.<br><b>Reaction:</b> After you announce a Battle action, if Lishan is at the current battlefield, target a Personality or Follower opposing her: Give it a Force penalty equal to Lishan's Personal Honor."
Utaku_Lishan = Personality(card_id=9083, title='Utaku Lishan', force=4, chi=3, personal_honor=3, gold_cost=9, honor_requirement=5, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])