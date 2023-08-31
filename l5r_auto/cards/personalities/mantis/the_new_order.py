from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Earth, Expendable, Kolat, Magistrate, Naval, Pirate, Samurai, Scout, Shugenja, TheMaskedWasp
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Kitsune_Gorikki = Personality(id=11909, title='Kitsune Gorikki', force=0, chi=3, honor_requirement=None, personal_honor=3, gold_cost=4, clan=[MantisClan], keywords=[Expendable, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kitsune_Yoshioka = Personality(id=11908, title='Kitsune Yoshioka', force=0, chi=2, honor_requirement=6, personal_honor=3, gold_cost=8, clan=[MantisClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Tsuruchi_Satou = Personality(id=11911, title='Tsuruchi Satou', force=2, chi=2, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[MantisClan], keywords=[Samurai, Scout, TheMaskedWasp], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yoritomo_Nishigori = Personality(id=11910, title='Yoritomo Nishigori', force=3, chi=3, honor_requirement=0, personal_honor=2, gold_cost=7, clan=[MantisClan], keywords=[Naval, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yoritomo_Raiden = Personality(id=11912, title='Yoritomo Raiden', force=4, chi=2, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[MantisClan], keywords=[Naval, Kolat, Pirate], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yoritomo_Yakuwa = Personality(id=11913, title='Yoritomo Yakuwa', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=3, clan=[MantisClan], keywords=[Naval, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])