from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Courtier, Duelist, Expendable, Imperial, Kensai, Monk, Reserve, Samurai, Shadowlands
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Daigotsu_Atsushi = Personality(id=11770, title='Daigotsu Atsushi', force=3, chi=3, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[SpiderClan], keywords=[Duelist, Expendable, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Daigotsu_Teruo = Personality(id=11771, title='Daigotsu Teruo', force=0, chi=1, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[SpiderClan, ShadowlandsFaction], keywords=[Expendable, Samurai, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Nao = Personality(id=11772, title='Nao', force=2, chi=3, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Kensai, Monk], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Sora = Personality(id=11773, title='Sora', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Kensai, Monk], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Susumu_Mizuki = Personality(id=11774, title='Susumu Mizuki', force=0, chi=2, honor_requirement=0, personal_honor=2, gold_cost=3, clan=[SpiderClan], keywords=[Reserve, Courtier], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Susumu_Takuan = Personality(id=11775, title='Susumu Takuan', force=2, chi=3, honor_requirement=0, personal_honor=2, gold_cost=7, clan=[SpiderClan], keywords=[Courtier, Imperial], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])