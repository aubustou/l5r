from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan, NinjaFaction
from l5r_auto.keywords import Courtier, Experienced, Imperial, Kensai, Kolat, LordOfBlades, LoveLetter, Merchant, Ninja, Samurai, Scout, Siege, Tactician, TheMaskedCrab, Unique
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Hida_Ayameko = Personality(id=11884, title='Hida Ayameko', force=3, chi=3, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[CrabClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Hida_Kenjiro = Personality(id=11888, title='Hida Kenjiro', force=3, chi=2, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[CrabClan], keywords=[Kensai, LordOfBlades, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Hida_OWin = Personality(id=11885, title='Hida O-Win', force=3, chi=3, honor_requirement=5, personal_honor=3, gold_cost=5, clan=[CrabClan], keywords=[Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Hiruma_Toshi = Personality(id=11886, title='Hiruma Toshi', force=2, chi=3, honor_requirement=None, personal_honor=0, gold_cost=3, clan=[CrabClan, NinjaFaction], keywords=[Ninja, Samurai, Scout, TheMaskedCrab], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kaiu_Akemi_the_Diplomat = Personality(id=11887, title='Kaiu Akemi, the Diplomat', force=3, chi=2, honor_requirement=3, personal_honor=2, gold_cost=4, clan=[CrabClan], keywords=[Courtier, LoveLetter, Samurai, Siege], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yasuki_Makoto_Imperial_Advisor_Experienced = Personality(id=11889, title='Yasuki Makoto, Imperial Advisor', force=2, chi=3, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[CrabClan], keywords=[Unique, Courtier, Experienced('1'), Imperial, Kolat, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])