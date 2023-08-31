from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import RatlingFaction, Unaligned
from l5r_auto.keywords import Nonhuman, Ratling
from l5r_auto.legality import DiamondEdition, LotusEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Ratling_Raider = Personality(id=6175, title='Ratling Raider', force=2, chi=2, honor_requirement=None, personal_honor=2, gold_cost=10, clan=[Unaligned, RatlingFaction], keywords=[Nonhuman, Ratling], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, LotusEdition, TwentyFestivalsEdition, DiamondEdition])