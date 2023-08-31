from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import SpiritFaction, Unaligned
from l5r_auto.keywords import Cavalry, Dog, Hunter, Nonhuman, Scout, Spirit
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
Karyuudo = Personality(id=4284, title='Karyuudo', force=2, chi=3, honor_requirement=2, personal_honor=3, gold_cost=4, clan=[SpiritFaction, Unaligned, SpiritFaction], keywords=[Cavalry, Dog, Hunter, Nonhuman, Scout, Spirit], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition, CelestialEdition])