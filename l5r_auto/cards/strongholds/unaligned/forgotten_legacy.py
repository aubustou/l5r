from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Forest, Temple
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'You do not gain Honor. You may not take Political actions. You do not lose Honor from cards you own. Before you lose Honor: Reduce the loss to 1, which may not be increased.<br><b>Limited:</b> Target your discarded Nonhuman Personality and discard a card in one of your provinces: Refill the province face-up with the Personality.'
The_Forgotten_Temple = Stronghold(card_id=8094, title='The Forgotten Temple', gold_production='4', starting_family_honor=-1, province_strength=7, clan=[Unaligned], keywords=[Forest, Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])