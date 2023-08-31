from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Courtier, Destined, Drunkard, Earth, Experienced, Hero, Jade, Magistrate, Merchant, Reserve, Samurai, Scout, Shugenja, Tactician, Unique
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Hida_Zaiberu = Personality(id=11728, title='Hida Zaiberu', force=4, chi=3, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[CrabClan], keywords=[Drunkard, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Hiruma_Maiko = Personality(id=11729, title='Hiruma Maiko', force=2, chi=2, honor_requirement=3, personal_honor=3, gold_cost=4, clan=[CrabClan], keywords=[Reserve, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kuni_Shinoda_Advisor_to_the_Jade_Champion_Experienced_2 = Personality(id=11730, title='Kuni Shinoda, Advisor to the Jade Champion', force=3, chi=3, honor_requirement=3, personal_honor=3, gold_cost=9, clan=[CrabClan], keywords=[Experienced('2'), Tactician, Unique, Earth, Hero, Jade, Magistrate, Scout, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Toritaka_Isai = Personality(id=11731, title='Toritaka Isai', force=3, chi=2, honor_requirement=0, personal_honor=2, gold_cost=6, clan=[CrabClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yasuki_Aitoko = Personality(id=11732, title='Yasuki Aitoko', force=0, chi=3, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[CrabClan], keywords=[Destined, Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yasuki_Shairei = Personality(id=11733, title='Yasuki Shairei', force=0, chi=2, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[CrabClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])