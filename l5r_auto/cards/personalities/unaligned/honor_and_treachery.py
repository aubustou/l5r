from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Experienced, Ronin, Samurai, Sober, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Battle:</b> Even if Tsubo is bowed, target a Personality: Straighten him.'
Tsubo_Experienced = Personality(card_id=10252, title='Tsubo', force=4, chi=4, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[Unaligned], keywords=[Experienced('Tsubo the Drunk'), Unique, Ronin, Samurai, Sober], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])