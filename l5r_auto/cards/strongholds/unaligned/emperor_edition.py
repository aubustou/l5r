from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import Unaligned
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'Your Ronin cards enter play for 1 less Gold and ignoring Honor Requirements.<br><b>Tireless Battle:</b> Give your chosen performing opposed Ronin Personality +2F.'
Palace_of_the_Breaking_Dawn = Stronghold(card_id=5863, title='Palace of the Breaking Dawn', gold_production='3', starting_family_honor=2, province_strength=7, clan=[Unaligned], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])