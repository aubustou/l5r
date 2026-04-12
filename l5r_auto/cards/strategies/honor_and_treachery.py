from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Target your performing Personality. <i>He undergoes vigorous training.</i> Permanently give him <b>Elite</b>. <i>(Elite cards contribute Force even if bowed.)</i>'
Elite_Training = Strategy(card_id=10255, title='Elite Training', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])