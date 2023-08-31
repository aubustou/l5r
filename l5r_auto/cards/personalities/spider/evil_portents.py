from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Conqueror, Destined, Duelist, Experienced, Infiltrator, Ninja, Nonhuman, Ogre, Resilient, Samurai, Shadowlands, Undead, Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Daigotsu_Aimaro = Personality(id=12482, title='Daigotsu Aimaro', force=2, chi=3, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[SpiderClan, ShadowlandsFaction], keywords=[Duelist, Samurai, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Daigotsu_Endo_Experienced = Personality(id=12483, title='Daigotsu Endo', force=4, chi=0, honor_requirement=None, personal_honor=0, gold_cost=8, clan=[SpiderClan, ShadowlandsFaction], keywords=[Destined, Experienced('1'), Nonhuman, Samurai, Shadowlands, Undead], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Daigotsu_Yuhmi_Experienced_2 = Personality(id=12484, title='Daigotsu Yuhmi', force=6, chi=2, honor_requirement=None, personal_honor=0, gold_cost=9, clan=[SpiderClan, ShadowlandsFaction], keywords=[Experienced('2'), Unique, Infiltrator, Nonhuman, Samurai, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Goju_Iaitsu = Personality(id=12485, title='Goju Iaitsu', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[SpiderClan, NinjaFaction, ShadowlandsFaction], keywords=[Ninja, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Goju_Toriken = Personality(id=12486, title='Goju Toriken', force=4, chi=3, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[SpiderClan, NinjaFaction, ShadowlandsFaction], keywords=[Conqueror, Ninja, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Hikayo = Personality(id=12487, title='Hikayo', force=5, chi=2, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[SpiderClan, ShadowlandsFaction], keywords=[Resilient, Nonhuman, Ogre, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])