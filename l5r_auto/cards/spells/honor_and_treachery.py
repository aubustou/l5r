from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Earth
from l5r_auto.legality import EmperorEdition, ModernEdition
"This Shugenja has <b>Stalwart</b>. <i>(Stalwart cards negate their first bowing each turn by other players' cards.)</i><br><b>Battle:</b> Target another of your Shugenja, who must be Earth: Transfer this card to him."
Communion_with_Earth = Spell(card_id=10254, title='Communion with Earth', gold_cost=0, focus_value=2, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])