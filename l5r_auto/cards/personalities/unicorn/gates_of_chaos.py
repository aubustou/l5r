from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, CommanderOfThe9thLegion, Courtier, DeathPriest, Destined, Experienced, Fallen, Imperial, IvoryChampion, Magistrate, Merchant, Paragon, Samurai, Scout, Shugenja, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>:bow::</b> Produce 3 Gold.'
Ide_Hinobu = Personality(card_id=10672, title='Ide Hinobu', force=0, chi=3, personal_honor=3, gold_cost=6, honor_requirement=4, clan=[UnicornClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'While you control any Ancestor Personalities or have any dead Personalities in your discard pile, Daiken has +1F.'
Moto_Daiken = Personality(card_id=10673, title='Moto Daiken', force=3, chi=4, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Home Battle:</b> Move Kinto home or, if he would be opposed, to the current battlefield. <i>(Home actions may be taken from home.)</i>'
Shinjo_Kinto_Experienced = Personality(card_id=10674, title='Shinjo Kinto', force=4, chi=3, personal_honor=2, gold_cost=9, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Unique, Commander, CommanderOfThe9thLegion, Experienced('1'), Imperial, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited, :g2::</b> Create a 1F <b>Cavalry </b> Follower and attach it to your target Personality.'
Shinjo_Tselu_Experienced_2 = Personality(card_id=10675, title='Shinjo Tselu', force=5, chi=5, personal_honor=3, gold_cost=10, honor_requirement=10, clan=[UnicornClan], keywords=[Cavalry, Experienced('2'), Unique, Commander, Imperial, IvoryChampion, Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br>After Yoshie enters play, lose 1 Honor.<br><b>Battle:</b> Give a target enemy Infantry Personality or Follower -3F.'
Shinjo_Yoshie = Personality(card_id=10676, title='Shinjo Yoshie', force=3, chi=1, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Destined, Commander, Fallen, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g3:: Give Sayaka two +1F tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Utaku_Sayaka = Personality(card_id=10671, title='Utaku Sayaka', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])