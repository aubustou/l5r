from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Earth, Experienced, Monk, Tattooed, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Draw a card.'
Togashi_Korimi_Experienced_2 = Personality(card_id=10222, title='Togashi Korimi', force=6, chi=4, personal_honor=2, gold_cost=11, honor_requirement=4, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Experienced('2'), Unique, Earth, Monk, Tattooed], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])