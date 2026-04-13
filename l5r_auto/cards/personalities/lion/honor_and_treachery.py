from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Samurai, SoulOf
from l5r_auto.legality import EmperorEdition, ModernEdition
"Before <i>(each time)</i> another player's action resolves during a battle at Shihiro's battlefield: Give Shihiro +1F <i>(until the turn ends)</i>."
Akodo_Shihiro = Personality(card_id=10241, title='Akodo Shihiro', force=3, chi=4, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[LionClan], keywords=[Samurai, SoulOf('Akodo Ieshige')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])