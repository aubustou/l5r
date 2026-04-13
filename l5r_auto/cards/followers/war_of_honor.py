from __future__ import annotations
from .common import Follower
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"<b>Battle:</b> Discard a card: Give this card a Force bonus equal to the discarded card's Focus Value <i>(until the turn ends)</i>."
Akodo_Regulars = Follower(card_id=262, title='Akodo Regulars', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=2, honor_requirement=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])