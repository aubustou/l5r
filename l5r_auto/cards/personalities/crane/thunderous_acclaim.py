from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Artisan, Courtier, Duelist, Expendable, Experienced, IronCrane, Magistrate, Poet, Resilient, Samurai, Spy, Storyteller, Yojimbo
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Daidoji_Kuraou = Personality(id=12290, title='Daidoji Kuraou', force=2, chi=2, honor_requirement=1, personal_honor=1, gold_cost=4, clan=[CraneClan], keywords=[IronCrane, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Doji_Buredo = Personality(id=12291, title='Doji Buredo', force=2, chi=2, honor_requirement=None, personal_honor=3, gold_cost=5, clan=[CraneClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Doji_Hoshihana = Personality(id=12292, title='Doji Hoshihana', force=1, chi=2, honor_requirement=4, personal_honor=3, gold_cost=5, clan=[CraneClan], keywords=[Artisan, Courtier, Poet, Storyteller], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Doji_Moro = Personality(id=12293, title='Doji Moro', force=2, chi=3, honor_requirement=5, personal_honor=3, gold_cost=5, clan=[CraneClan], keywords=[Resilient, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kakita_Iwari = Personality(id=12294, title='Kakita Iwari', force=1, chi=3, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[CraneClan], keywords=[Expendable, Artisan, Courtier, Spy], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kakita_Shinichi_Experienced = Personality(id=12295, title='Kakita Shinichi', force=3, chi=4, honor_requirement=5, personal_honor=3, gold_cost=9, clan=[CraneClan], keywords=[Duelist, Resilient, Experienced('1'), Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])