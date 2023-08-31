from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, DeathPriest, Destined, Experienced, Magistrate, Naval, Resilient, Samurai, Shugenja, Water
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Moto_Chinua_Experienced = Personality(id=12493, title='Moto Chinua', force=3, chi=3, honor_requirement=0, personal_honor=2, gold_cost=7, clan=[UnicornClan], keywords=[Cavalry, Experienced('1'), Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Moto_Daiketsu = Personality(id=12494, title='Moto Dai-ketsu', force=3, chi=3, honor_requirement=None, personal_honor=1, gold_cost=8, clan=[UnicornClan], keywords=[Cavalry, Naval, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Moto_Jengzan = Personality(id=12495, title='Moto Jengzan', force=3, chi=2, honor_requirement=0, personal_honor=1, gold_cost=4, clan=[UnicornClan], keywords=[Resilient, Commander, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Shinjo_Dogenda = Personality(id=12496, title='Shinjo Dogenda', force=2, chi=4, honor_requirement=4, personal_honor=3, gold_cost=7, clan=[UnicornClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Shinjo_Megura = Personality(id=12497, title='Shinjo Megura', force=2, chi=2, honor_requirement=7, personal_honor=3, gold_cost=5, clan=[UnicornClan], keywords=[Cavalry, Destined, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Utaku_Yabusame = Personality(id=12498, title='Utaku Yabusame', force=3, chi=3, honor_requirement=6, personal_honor=3, gold_cost=8, clan=[UnicornClan], keywords=[Cavalry, BattleMaiden, Commander, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])