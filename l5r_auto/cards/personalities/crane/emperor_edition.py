from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Commander, IronCrane, Samurai, Scout, SoulOf
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
Daidoji_Tametaka = Personality(id=1682, title='Daidoji Tametaka', force=4, chi=3, honor_requirement=4, personal_honor=2, gold_cost=8, clan=[CraneClan], keywords=[Commander, IronCrane, Samurai, Scout, SoulOf('Daidoji Zoushi')], traits=[], abilities=[], legality=[ModernEdition, EmperorEdition, IvoryEdition, TwentyFestivalsEdition])