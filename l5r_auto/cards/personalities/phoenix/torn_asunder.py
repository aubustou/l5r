from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Fire, Shugenja
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
Isawa_Hibana = Personality(id=10305, title='Isawa Hibana', force=3, chi=3, honor_requirement=6, personal_honor=2, gold_cost=6, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[ModernEdition, EmperorEdition, IvoryEdition, TwentyFestivalsEdition])