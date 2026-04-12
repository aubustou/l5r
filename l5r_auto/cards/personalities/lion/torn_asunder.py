from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Apprentice, Artisan, Cavalry, Experienced, Messenger, Paragon, Samurai, Scout, Shugenja, Tactician, TurquoiseChampion, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
"Crab Clan players may ignore Chiyo's Honor Requirement.<br><b>Battle:</b> Melee 4 Attack."
Akodo_Chiyo = Personality(card_id=10290, title='Akodo Chiyo', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Show a card in your hand and choose another player: <i>You offer him a gift.</i> He may put the card in his hand; if he does, draw two cards. Otherwise, discard it, and Melee Attack with strength equal to its Focus Value targeting a Follower or Personality without Followers in his home.'
Ikoma_Satoru_Experienced = Personality(card_id=10291, title='Ikoma Satoru', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Unique, Artisan, Experienced('1'), Samurai, TurquoiseChampion], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow Shizuka: Search you Dynasty or Fate deck. If you find a Region, attach it to one of your provinces, paying all costs. If you find a Terrain, put it in your hand and discard a card.'
Ikoma_Shizuka = Personality(card_id=10292, title='Ikoma Shizuka', force=2, chi=3, personal_honor=2, gold_cost=5, honor_requirement=3, clan=[LionClan], keywords=[Cavalry, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If Miwa is face-up in your province, discard her and pay 2 Gold: Search your Dynasty deck for a non-Unique Lion Clan Shugenja. Refill this province with him, face-up.'
Kitsu_Miwa = Personality(card_id=10293, title='Kitsu Miwa', force=0, chi=2, personal_honor=3, gold_cost=5, honor_requirement=7, clan=[LionClan], keywords=[Apprentice, Messenger, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will not attach Items.<br>During battle resolution, if Sango is attacking, he contributes his Force twice.'
Matsu_Sango = Personality(card_id=10294, title='Matsu Sango', force=1, chi=3, personal_honor=3, gold_cost=5, honor_requirement=7, clan=[LionClan], keywords=[Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Yoshito has +1F while attacking, or +2F if the Defender is Dragon Clan.'
Matsu_Yoshito = Personality(card_id=10295, title='Matsu Yoshito', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Cavalry, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])