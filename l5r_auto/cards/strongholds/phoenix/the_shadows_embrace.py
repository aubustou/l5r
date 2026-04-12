from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import PhoenixClan
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Put a Spell from your hand face-up underneath this card.<br><b>Battle:</b> Any number of times per turn, discard a Spell from under this card: Either straighten one to three Shugenja at the current battlefield if the Spell is Air or Water, or Ranged 4 Attack if it is Earth or Fire, or draw a card if it is Void.'
The_New_Foundries = Stronghold(card_id=9947, title='The New Foundries', gold_production='4', starting_family_honor=6, province_strength=6, clan=[PhoenixClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])