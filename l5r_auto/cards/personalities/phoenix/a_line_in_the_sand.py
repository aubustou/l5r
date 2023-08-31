from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Air, Cavalry, Destined, Earth, Fire, Resilient, Samurai, Shugenja, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Agasha_Beiru = Personality(id=11592, title='Agasha Beiru', force=1, chi=3, honor_requirement=6, personal_honor=3, gold_cost=4, clan=[PhoenixClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Isawa_Kaisei = Personality(id=11593, title='Isawa Kaisei', force=0, chi=3, honor_requirement=6, personal_honor=4, gold_cost=7, clan=[PhoenixClan], keywords=[Cavalry, Destined, Air, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Isawa_Orinoko = Personality(id=11594, title='Isawa Orinoko', force=2, chi=2, honor_requirement=None, personal_honor=3, gold_cost=5, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Isawa_Waiko = Personality(id=11595, title='Isawa Waiko', force=3, chi=3, honor_requirement=4, personal_honor=1, gold_cost=7, clan=[PhoenixClan], keywords=[Resilient, Fire, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shiba_Tuoko = Personality(id=11596, title='Shiba Tuoko', force=3, chi=3, honor_requirement=4, personal_honor=2, gold_cost=7, clan=[PhoenixClan], keywords=[Resilient, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shiba_Yinfuo = Personality(id=11597, title='Shiba Yinfuo', force=2, chi=2, honor_requirement=4, personal_honor=3, gold_cost=5, clan=[PhoenixClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])