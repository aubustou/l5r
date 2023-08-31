from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, NinjaFaction, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Assassin, Conqueror, Courtier, Kensai, Monk, Naval, Ninja, Reserve, Resilient, Samurai, Shadowlands
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Daigotsu_Jemaru = Personality(id=11604, title='Daigotsu Jemaru', force=4, chi=2, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[SpiderClan, ShadowlandsFaction], keywords=[Reserve, Resilient, Samurai, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Goju_Saido = Personality(id=11605, title='Goju Saido', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[SpiderClan, NinjaFaction, ShadowlandsFaction], keywords=[Assassin, Ninja, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Marimako = Personality(id=11606, title='Marimako', force=3, chi=1, honor_requirement=0, personal_honor=0, gold_cost=4, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Conqueror, Kensai, Naval, Monk], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Susumu_Jaru = Personality(id=11607, title='Susumu Jaru', force=1, chi=1, honor_requirement=0, personal_honor=2, gold_cost=6, clan=[SpiderClan], keywords=[Courtier], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Susumu_Tanjin = Personality(id=11608, title='Susumu Tanjin', force=0, chi=2, honor_requirement=0, personal_honor=1, gold_cost=2, clan=[SpiderClan], keywords=[Courtier], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yasi = Personality(id=11609, title='Yasi', force=4, chi=2, honor_requirement=None, personal_honor=0, gold_cost=8, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Kensai, Resilient, Monk], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])