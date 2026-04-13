from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, EmeraldChampion, Experienced, Imperial, IvoryChampion, Magistrate, Paragon, Samurai, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
'After Shaocheng enters play: Turn a card in a province face-up. If it is a non-Unique Personality, discard him and he becomes honorably dead.'
Iuchi_Shaocheng = Personality(card_id=10325, title='Iuchi Shaocheng', force=2, chi=2, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Ogaru has +1F while the enemy leader controls an Imperial card or the Imperial Favor.'
Moto_Ogaru = Personality(card_id=10326, title='Moto Ogaru', force=3, chi=1, personal_honor=2, gold_cost=5, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After your Tactical action resolves: Give a Personality who performed it +2F.'
Shinjo_Sihung = Personality(card_id=10327, title='Shinjo Sihung', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Cavalry Followers attach to your Personalities paying 2 less Gold.<br>After another player's action resolves which targeted Tselu: That player discards a card."
Shinjo_Tselu = Personality(card_id=10328, title='Shinjo Tselu', force=5, chi=4, personal_honor=3, gold_cost=10, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Unique, Commander, Imperial, IvoryChampion, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Your dishonorable Paragons do not have a maximum Personal Honor of 0 from the rulebook.<br><b>Reaction:</b> After engaging at Ji-Yun's battlefield, target a Personality opposing her: He may not use his abilities."
Utaku_JiYun_Experienced = Personality(card_id=10329, title='Utaku Ji-Yun', force=5, chi=4, personal_honor=4, gold_cost=9, honor_requirement=5, clan=[UnicornClan], keywords=[Cavalry, Unique, BattleMaiden, EmeraldChampion, Experienced('1'), Imperial, Magistrate, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After a battle resolution in which Suying's army destroyed a defending army or province: Gain 2 Honor."
Utaku_Suying = Personality(card_id=10330, title='Utaku Suying', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])