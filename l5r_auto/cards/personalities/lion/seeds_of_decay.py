from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Brash, Courtier, Experienced, Imperial, Loyal, Paragon, Samurai, Scout, Sensei, Shugenja, Tactician, Unique, Water, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
"Hotaka has +1PH if any other player is Dragon Clan.<br>Hotaka may not perform Dark Virtue actions.<br>The amount of Honor you need in order to win an Honor Victory is reduced by Hotaka's Personal Honor minus one."
Akodo_Hotaka = Personality(card_id=10059, title='Akodo Hotaka', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy a target enemy attachment.'
Akodo_Michitsu = Personality(card_id=10060, title='Akodo Michitsu', force=2, chi=3, personal_honor=3, gold_cost=6, honor_requirement=4, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Aimi enters play: Discard all your other Sensei Personalities.<br>Your Lion Clan Personalities <i>(in play)</i> have <b>Courtier </b>but do not have <b>Cavalry, Commander, Deathseeker, Paragon, Scout, </b>or<b> Tactician</b>.'
Ikoma_Aimi = Personality(card_id=10061, title='Ikoma Aimi', force=3, chi=4, personal_honor=2, gold_cost=7, honor_requirement=5, clan=[LionClan], keywords=[Loyal, Courtier, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(The Defender may draw a card after a Brash card is assigned to attack.)</i><br><b>Battle:</b> Target an enemy card without attachments: Bow it.'
Ikoma_Masumi = Personality(card_id=10062, title='Ikoma Masumi', force=4, chi=2, personal_honor=2, gold_cost=6, honor_requirement=4, clan=[LionClan], keywords=[Brash, Imperial, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow Kouki and target an enemy Personality: Give him -3F.'
Kitsu_Kouki = Personality(card_id=10063, title='Kitsu Kouki', force=0, chi=3, personal_honor=3, gold_cost=5, honor_requirement=4, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Give each other Lion Clan Personality in your army a Force bonus equal to his own Personal Honor.'
Matsu_Koyama_Experienced = Personality(card_id=10064, title='Matsu Koyama', force=5, chi=4, personal_honor=4, gold_cost=9, honor_requirement=10, clan=[LionClan], keywords=[Unique, Experienced('1'), Imperial, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])