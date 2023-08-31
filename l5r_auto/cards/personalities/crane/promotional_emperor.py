from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Duelist, Samurai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Kakita_Izumiko = Personality(id=10576, title='Kakita Izumiko', force=2, chi=3, honor_requirement=6, personal_honor=3, gold_cost=5, clan=[CraneClan], keywords=[Duelist, Samurai], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, IvoryEdition, EmperorEdition, TwentyFestivalsEdition])