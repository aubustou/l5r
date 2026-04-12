from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan, ShadowlandsFaction
from l5r_auto.keywords import Berserker, Damned, Experienced, Shadowlands, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Reaction:</b> After another player's Battle action resolves, if its effects destroyed Yamadera: Melee 8 Attack."
Hida_Yamadera_Experienced = Personality(card_id=10220, title='Hida Yamadera', force=8, chi=3, personal_honor=0, gold_cost=12, honor_requirement=None, clan=[CrabClan, ShadowlandsFaction], keywords=[Unique, Berserker, Damned, Experienced('1'), Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])