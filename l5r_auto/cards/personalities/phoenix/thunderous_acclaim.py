from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Earth, Expendable, Experienced, Fire, Inquisitor, Magistrate, Reserve, Resilient, Samurai, Scholar, Shugenja, Water, Yojimbo
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Asako_Kazuki = Personality(id=12314, title='Asako Kazuki', force=0, chi=1, honor_requirement=6, personal_honor=3, gold_cost=5, clan=[PhoenixClan], keywords=[Resilient, Earth, Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Asako_Nashimoto = Personality(id=12315, title='Asako Nashimoto', force=4, chi=3, honor_requirement=None, personal_honor=3, gold_cost=8, clan=[PhoenixClan], keywords=[Resilient, Earth, Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Fujisawa = Personality(id=12316, title='Isawa Fujisawa', force=2, chi=5, honor_requirement=2, personal_honor=1, gold_cost=6, clan=[PhoenixClan], keywords=[Reserve, Scholar, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Hibana_Experienced = Personality(id=12317, title='Isawa Hibana', force=4, chi=4, honor_requirement=6, personal_honor=3, gold_cost=10, clan=[PhoenixClan], keywords=[Experienced('1'), Fire, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Isawa_Nobuo = Personality(id=12318, title='Isawa Nobuo', force=2, chi=2, honor_requirement=2, personal_honor=1, gold_cost=4, clan=[PhoenixClan], keywords=[Expendable, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Shiba_Hano = Personality(id=12319, title='Shiba Hano', force=3, chi=2, honor_requirement=5, personal_honor=3, gold_cost=6, clan=[PhoenixClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])