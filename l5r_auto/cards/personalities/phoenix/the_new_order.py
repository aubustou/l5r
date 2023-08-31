from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Air, Cavalry, Destined, Duelist, Fire, LoveLetter, Naval, Nonhuman, Orochi, Samurai, ScionOfFlame, ScionOfTheSea, Shugenja, Water, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Isawa_Fujigawa = Personality(id=11916, title='Isawa Fujigawa', force=3, chi=4, honor_requirement=4, personal_honor=2, gold_cost=6, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Isawa_Nomura = Personality(id=11914, title='Isawa Nomura', force=2, chi=2, honor_requirement=6, personal_honor=2, gold_cost=5, clan=[PhoenixClan], keywords=[Fire, ScionOfFlame, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Isawa_Tenkawa_the_Scholar = Personality(id=11915, title='Isawa Tenkawa, the Scholar', force=0, chi=5, honor_requirement=6, personal_honor=3, gold_cost=5, clan=[PhoenixClan], keywords=[Air, LoveLetter, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kyuji = Personality(id=11917, title='Kyuji', force=3, chi=4, honor_requirement=9, personal_honor=3, gold_cost=7, clan=[PhoenixClan], keywords=[Cavalry, Naval, Nonhuman, Orochi, ScionOfTheSea, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shiba_Kintaro_the_Remembered = Personality(id=11919, title='Shiba Kintaro, the Remembered', force=2, chi=3, honor_requirement=5, personal_honor=3, gold_cost=5, clan=[PhoenixClan], keywords=[Destined, Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shiba_Koshiba = Personality(id=11918, title='Shiba Koshiba', force=3, chi=2, honor_requirement=1, personal_honor=1, gold_cost=4, clan=[PhoenixClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])