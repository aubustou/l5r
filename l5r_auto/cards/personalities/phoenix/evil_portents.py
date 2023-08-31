from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Air, Alchemist, Cavalry, Earth, Experienced, Inquisitor, Jade, Loyal, Magistrate, Resilient, Samurai, Shugenja, TheMaskedPhoenix, Unique, Void, Water, Yojimbo
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Agasha_Dorai = Personality(id=12470, title='Agasha Dorai', force=2, chi=3, honor_requirement=None, personal_honor=2, gold_cost=5, clan=[PhoenixClan], keywords=[Air, Alchemist, Shugenja, Void], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Asako_Misai = Personality(id=12471, title='Asako Misai', force=2, chi=4, honor_requirement=2, personal_honor=3, gold_cost=6, clan=[PhoenixClan], keywords=[Earth, Inquisitor, Magistrate, Shugenja, TheMaskedPhoenix], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Bikaru = Personality(id=12472, title='Isawa Bikaru', force=4, chi=4, honor_requirement=3, personal_honor=3, gold_cost=8, clan=[PhoenixClan], keywords=[Resilient, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Hokaiko = Personality(id=12473, title='Isawa Hokaiko', force=3, chi=3, honor_requirement=6, personal_honor=2, gold_cost=7, clan=[PhoenixClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Norimichi_Elemental_Master_Experienced_2 = Personality(id=12474, title='Isawa Norimichi, Elemental Master', force=5, chi=5, honor_requirement=6, personal_honor=3, gold_cost=11, clan=[PhoenixClan], keywords=[Experienced('2'), Loyal, Unique, Earth, Jade, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Shiba_Kakei_Experienced = Personality(id=12475, title='Shiba Kakei', force=3, chi=3, honor_requirement=6, personal_honor=3, gold_cost=8, clan=[PhoenixClan], keywords=[Cavalry, Experienced('1'), Samurai, Void, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])