from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Brash, Cavalry, Commander, Conqueror, DeathPriest, Loyal, Paragon, Samurai, Shogun, Shugenja, StableMaster, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Battle/Open:</b> Even if Aoi is at home, bow him and target a Personality: Give him +4F.'
Moto_Aoi = Personality(card_id=10098, title='Moto Aoi', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Moto_Miyu = Personality(card_id=10099, title='Moto Miyu', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=0, clan=[UnicornClan], keywords=[Cavalry, Conqueror, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Taigo may perform up to three Tactical actions per turn.<br><b>Tactical Battle:</b> Target an enemy Personality: Bow him. If he is Infantry, you may target and destroy a card without attachments in his unit.'
Moto_Taigo = Personality(card_id=10100, title='Moto Taigo', force=4, chi=4, personal_honor=2, gold_cost=11, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Conqueror, Loyal, Tactician, Unique, Commander, Samurai, Shogun], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Katsuo does not have Brash if any other player is Lion Clan. <i>(The Defender may draw a card after a Brash card is assigned to attack.)</i><br><b>Battle/Open:</b> Target your Follower: Straighten it. You may take an additional action.'
Shinjo_Katsuo = Personality(card_id=10101, title='Shinjo Katsuo', force=4, chi=2, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[UnicornClan], keywords=[Brash, Cavalry, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your dishonorable Battle Maidens do not have a maximum Personal Honor of 0 from the rulebook.<br><b>Limited:</b> Gain 2 Honor. You may not declare an attack this turn.'
Utaku_Chikako = Personality(card_id=10102, title='Utaku Chikako', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=8, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Bow Hirononri and target a Stables or Cavalry card: Straighten it.'
Utaku_Hirononri = Personality(card_id=10103, title='Utaku Hirononri', force=0, chi=1, personal_honor=1, gold_cost=3, honor_requirement=0, clan=[UnicornClan], keywords=[StableMaster], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])