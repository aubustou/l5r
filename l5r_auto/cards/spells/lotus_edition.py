from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Maho
from l5r_auto.legality import ImperialEdition, IvoryEdition, LotusEdition, ModernEdition, TwentyFestivalsEdition
'<b>Maho Limited:</b> Bow this Shugenja and destroy this Spell to create a 5F/2C <b>Champion &#149; Shadowlands &#149; Undead</b> Personality and lose 4 Honor.'
Summon_Undead_Champion = Spell(card_id=7636, title='Summon Undead Champion', gold_cost=3, focus_value=2, keywords=[Maho], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, ImperialEdition, ModernEdition])