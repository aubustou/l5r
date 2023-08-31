from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Artisan, Courtier, Duelist, Expendable, Experienced, Jester, Kensai, Magistrate, Resilient, Samurai, TheMaskedCrane
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Doji_Ikei = Personality(id=12446, title='Doji Ikei', force=2, chi=2, honor_requirement=6, personal_honor=2, gold_cost=4, clan=[CraneClan], keywords=[Resilient, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Doji_Natsuyo_Experienced = Personality(id=12447, title='Doji Natsuyo', force=1, chi=4, honor_requirement=8, personal_honor=3, gold_cost=6, clan=[CraneClan], keywords=[Courtier, Experienced('1')], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Doji_Soeka_Experienced = Personality(id=12448, title='Doji Soeka', force=2, chi=4, honor_requirement=6, personal_honor=3, gold_cost=6, clan=[CraneClan], keywords=[Courtier, Experienced('1'), Magistrate], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kakita_Daitsu_Experienced = Personality(id=12449, title='Kakita Daitsu', force=3, chi=4, honor_requirement=5, personal_honor=3, gold_cost=8, clan=[CraneClan], keywords=[Duelist, Kensai, Experienced('1'), Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kakita_Inaka = Personality(id=12450, title='Kakita Inaka', force=0, chi=3, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[CraneClan], keywords=[Artisan, Courtier, Jester], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kakita_Oshaberi = Personality(id=12451, title='Kakita Oshaberi', force=1, chi=3, honor_requirement=4, personal_honor=1, gold_cost=5, clan=[CraneClan], keywords=[Expendable, Artisan, Courtier, TheMaskedCrane], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])