from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import CrabClan
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Battle:</b> Target your performing Berserker or unbowed Personality. Destroy a target enemy card with lower Force and no attachments.'
Bishamons_Tower = Stronghold(card_id=9945, title="Bishamon's Tower", gold_production='4', starting_family_honor=3, province_strength=8, clan=[CrabClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])