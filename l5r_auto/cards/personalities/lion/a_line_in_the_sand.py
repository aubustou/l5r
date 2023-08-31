from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Deathseeker, Resilient, Samurai, Scout, Shugenja, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Akodo_Niito = Personality(id=11580, title='Akodo Niito', force=2, chi=3, honor_requirement=7, personal_honor=3, gold_cost=6, clan=[LionClan], keywords=[Resilient, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Ikoma_Akinari = Personality(id=11581, title='Ikoma Akinari', force=3, chi=3, honor_requirement=4, personal_honor=3, gold_cost=5, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Ikoma_Genichi = Personality(id=11582, title='Ikoma Genichi', force=2, chi=2, honor_requirement=10, personal_honor=3, gold_cost=6, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kitsu_Junsuke = Personality(id=11583, title='Kitsu Junsuke', force=1, chi=4, honor_requirement=2, personal_honor=2, gold_cost=6, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kitsu_Watanabe = Personality(id=11584, title='Kitsu Watanabe', force=1, chi=3, honor_requirement=7, personal_honor=3, gold_cost=4, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Matsu_Rishou = Personality(id=11585, title='Matsu Rishou', force=4, chi=1, honor_requirement=2, personal_honor=2, gold_cost=4, clan=[LionClan], keywords=[Deathseeker, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])