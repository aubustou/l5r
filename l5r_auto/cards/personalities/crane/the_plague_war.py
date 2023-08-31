from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Duelist, Kenku, Nonhuman
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Shune = Personality(id=7236, title='Shune', force=1, chi=4, honor_requirement=4, personal_honor=3, gold_cost=6, clan=[CraneClan], keywords=[Duelist, Kenku, Nonhuman], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition, CelestialEdition])