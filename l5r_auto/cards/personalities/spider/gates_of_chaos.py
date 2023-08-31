from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Destined, Fallen, Kensai, Monk, Paragon, Samurai, Shadowlands
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Daigotsu_Ryuko = Personality(id=10660, title='Daigotsu Ryuko', force=3, chi=2, honor_requirement=None, personal_honor=0, gold_cost=7, clan=[SpiderClan, ShadowlandsFaction], keywords=[Destined, Fallen, Paragon, Samurai, Shadowlands], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, IvoryEdition, EmperorEdition, TwentyFestivalsEdition])
Laoshe = Personality(id=10663, title='Lao-she', force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Kensai, Monk], traits=[], abilities=[], legality=[OnyxEdition, ModernEdition, IvoryEdition, EmperorEdition, TwentyFestivalsEdition])