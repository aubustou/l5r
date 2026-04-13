from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Political
from l5r_auto.legality import ImperialEdition, ModernEdition, TwentyFestivalsEdition
'You can only play one Legendary Victory per battle.<br><b>Political Battle:</b> If you are the Attacker or Defender in this battle and your army is currently opposed by an army with greater total Force, double your Honor gains during the Resolution Segment after all other bonuses are applied.'
Legendary_Victory = Strategy(card_id=4696, title='Legendary Victory', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, ModernEdition])