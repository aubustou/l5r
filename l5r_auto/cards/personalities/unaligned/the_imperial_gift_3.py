from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Duelist, Ronin, Samurai
from l5r_auto.legality import CelestialEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Seasoned_Ronin = Personality(id=6532, title='Seasoned Ronin', force=3, chi=3, honor_requirement=1, personal_honor=2, gold_cost=5, clan=[Unaligned], keywords=[Ronin, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition, CelestialEdition])
Tarui = Personality(id=7821, title='Tarui', force=2, chi=3, honor_requirement=None, personal_honor=0, gold_cost=3, clan=[Unaligned], keywords=[Duelist, Ronin, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition, CelestialEdition])