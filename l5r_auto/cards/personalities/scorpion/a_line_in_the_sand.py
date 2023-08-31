from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Air, Cavalry, Conqueror, Courtier, Ninja, Reserve, Resilient, Samurai, Scout, Shugenja, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Bayushi_Atsuto = Personality(id=11598, title='Bayushi Atsuto', force=3, chi=2, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[ScorpionClan], keywords=[Conqueror, Courtier, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_Yasunari = Personality(id=11599, title='Bayushi Yasunari', force=3, chi=1, honor_requirement=0, personal_honor=1, gold_cost=4, clan=[ScorpionClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shosuro_Kiyofumi = Personality(id=11600, title='Shosuro Kiyofumi', force=2, chi=2, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[ScorpionClan, NinjaFaction], keywords=[Resilient, Ninja, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shosuro_Yasumasa = Personality(id=11601, title='Shosuro Yasumasa', force=1, chi=4, honor_requirement=None, personal_honor=1, gold_cost=7, clan=[ScorpionClan], keywords=[Courtier], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Soshi_Kitaiko = Personality(id=11602, title='Soshi Kitaiko', force=0, chi=3, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[ScorpionClan], keywords=[Air, Courtier, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yogo_Gingo = Personality(id=11603, title='Yogo Gingo', force=2, chi=2, honor_requirement=None, personal_honor=2, gold_cost=5, clan=[ScorpionClan], keywords=[Cavalry, Reserve, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])