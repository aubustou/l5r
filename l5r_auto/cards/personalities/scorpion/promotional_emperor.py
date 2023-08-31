from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import BitterLies, Conqueror, Samurai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Bayushi_Aibako = Personality(id=10581, title='Bayushi Aibako', force=3, chi=3, honor_requirement=None, personal_honor=2, gold_cost=5, clan=[ScorpionClan], keywords=[Conqueror, BitterLies, Samurai], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, IvoryEdition, EmperorEdition, TwentyFestivalsEdition])