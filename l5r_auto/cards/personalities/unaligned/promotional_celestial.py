from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Ronin, Shugenja, Void
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Enomoto = Personality(id=2348, title='Enomoto', force=3, chi=2, honor_requirement=6, personal_honor=2, gold_cost=5, clan=[Unaligned], keywords=[Ronin, Shugenja, Void], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition, CelestialEdition])