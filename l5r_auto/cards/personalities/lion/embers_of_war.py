from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Shugenja, SodanSenzo, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
Kitsu_Miro = Personality(id=4386, title='Kitsu Miro', force=3, chi=3, honor_requirement=6, personal_honor=3, gold_cost=5, clan=[LionClan], keywords=[Shugenja, SodanSenzo, Water], traits=[], abilities=[], legality=[ModernEdition, EmperorEdition, IvoryEdition, TwentyFestivalsEdition])