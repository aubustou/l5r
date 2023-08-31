from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Alchemist, Cavalry, Duelist, Earth, Kensai, Magistrate, Monk, Reserve, Resilient, Samurai, Shugenja, Tattooed, Void
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Mirumoto_Futoro = Personality(id=11574, title='Mirumoto Futoro', force=2, chi=2, honor_requirement=4, personal_honor=3, gold_cost=5, clan=[DragonClan], keywords=[Cavalry, Duelist, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Mirumoto_Jaikei = Personality(id=11575, title='Mirumoto Jaikei', force=3, chi=1, honor_requirement=0, personal_honor=1, gold_cost=5, clan=[DragonClan], keywords=[Kensai, Reserve, Resilient, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Mirumoto_Saiko = Personality(id=11576, title='Mirumoto Saiko', force=2, chi=3, honor_requirement=4, personal_honor=2, gold_cost=6, clan=[DragonClan], keywords=[Kensai, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Tamori_Ginrao = Personality(id=11577, title='Tamori Ginrao', force=2, chi=3, honor_requirement=5, personal_honor=3, gold_cost=5, clan=[DragonClan], keywords=[Earth, Magistrate, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Tamori_Wataru = Personality(id=11578, title='Tamori Wataru', force=1, chi=5, honor_requirement=0, personal_honor=2, gold_cost=6, clan=[DragonClan], keywords=[Alchemist, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Togashi_Shao = Personality(id=11579, title='Togashi Shao', force=2, chi=4, honor_requirement=None, personal_honor=0, gold_cost=6, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Resilient, Monk, Tattooed, Void], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])