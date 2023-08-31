from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Commander, Nonhuman, Shadowlands, Undead, Zombie
from l5r_auto.legality import GoldEdition, IvoryEdition, JadeEdition, ModernEdition, TwentyFestivalsEdition
Noekam = Personality(id=5611, title='Noekam', force=4, chi=3, honor_requirement=None, personal_honor=0, gold_cost=8, clan=[Unaligned, ShadowlandsFaction], keywords=[Commander, Nonhuman, Shadowlands, Undead, Zombie], traits=[], abilities=[], legality=[ModernEdition, GoldEdition, JadeEdition, IvoryEdition, TwentyFestivalsEdition])