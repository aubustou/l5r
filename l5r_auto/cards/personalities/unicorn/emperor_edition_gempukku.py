from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import Cavalry, Experienced, Samurai, Tactician, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Reaction:</b> After a Tactical Battle action resolves that Byung performed: Take an additional Battle action.'
Shinjo_Byung_Experienced = Personality(card_id=10228, title='Shinjo Byung', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Tactician, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])