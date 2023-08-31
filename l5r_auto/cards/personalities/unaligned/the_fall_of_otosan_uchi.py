from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NagaFaction, Unaligned
from l5r_auto.keywords import Constrictor, Naga, Nonhuman
from l5r_auto.legality import DiamondEdition, GoldEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Chaldera = Personality(id=1289, title='Chaldera', force=4, chi=2, honor_requirement=2, personal_honor=2, gold_cost=7, clan=[Unaligned, NagaFaction], keywords=[Constrictor, Naga, Nonhuman], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, GoldEdition, TwentyFestivalsEdition, DiamondEdition])