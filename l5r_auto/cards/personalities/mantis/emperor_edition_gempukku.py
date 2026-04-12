from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Experienced, Scout, Shugenja, Thunder, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> If you have attached a card from your hand this turn, bow Madoka: Draw a card.'
Moshi_Madoka_Experienced = Personality(card_id=10224, title='Moshi Madoka', force=3, chi=3, personal_honor=2, gold_cost=6, honor_requirement=2, clan=[MantisClan], keywords=[Unique, Experienced('1'), Scout, Shugenja, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])