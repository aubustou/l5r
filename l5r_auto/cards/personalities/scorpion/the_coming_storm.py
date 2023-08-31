from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import BitterLies, Courtier, Expendable, Junshin, Kensai, Mastermind, Ninja, SakeAddict, Samurai, Spy, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Bayushi_Akagi = Personality(id=11764, title='Bayushi Akagi', force=3, chi=3, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[ScorpionClan], keywords=[Kensai, BitterLies, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_Fuyuko = Personality(id=11765, title='Bayushi Fuyuko', force=1, chi=3, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[ScorpionClan], keywords=[Courtier], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_JinnJa = Personality(id=11766, title='Bayushi Jinn-Ja', force=0, chi=3, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[ScorpionClan], keywords=[Courtier, Mastermind, SakeAddict], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_Kotomuri = Personality(id=11767, title='Bayushi Kotomuri', force=3, chi=2, honor_requirement=None, personal_honor=3, gold_cost=6, clan=[ScorpionClan], keywords=[Expendable, Junshin, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shosuro_Kayo = Personality(id=11768, title='Shosuro Kayo', force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[ScorpionClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shosuro_Sadao = Personality(id=11769, title='Shosuro Sadao', force=2, chi=2, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja, Samurai, Spy], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])