from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Commander, Conqueror, Experienced, Loyal, Samurai, Shadowlands, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
"After Negishi enters play: Lose 2 Honor.<br>Negate Negishi's destruction from effects of actions performed by any Personality whose unit's total Gold Cost was lower than Negishi's unit's <i>(when they performed it)</i>."
Daigotsu_Negishi_Experienced = Personality(card_id=10227, title='Daigotsu Negishi', force=5, chi=2, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[SpiderClan, ShadowlandsFaction], keywords=[Conqueror, Loyal, Unique, Commander, Experienced('1'), Samurai, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])