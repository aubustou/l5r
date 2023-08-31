from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Samurai, Shadowlands
from l5r_auto.legality import DiamondEdition, IvoryEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
Daigotsu_Meguro = Personality(id=1745, title='Daigotsu Meguro', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[SpiderClan, ShadowlandsFaction], keywords=[Samurai, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, SamuraiEdition, IvoryEdition, TwentyFestivalsEdition, DiamondEdition])