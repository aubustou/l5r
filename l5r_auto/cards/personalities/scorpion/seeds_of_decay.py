from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Ninja
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Soshi_Kodanshi = Personality(id=10082, title='Soshi Kodanshi', force=4, chi=3, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja], traits=[], abilities=[], legality=[ModernEdition, EmperorEdition, OnyxEdition, TwentyFestivalsEdition])