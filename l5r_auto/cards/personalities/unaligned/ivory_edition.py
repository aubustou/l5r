from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, Unaligned
from l5r_auto.keywords import Actor, Duelist, Fire, Kensai, Monk, Ronin, Samurai, Shugenja, SoulOf, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Dainiko = Personality(id=11229, title='Dainiko', force=0, chi=3, honor_requirement=0, personal_honor=2, gold_cost=5, clan=[Unaligned, BrotherhoodOfShinsei], keywords=[Fire, Monk, Ronin, SoulOf('Nakadai')], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Horobei = Personality(id=11230, title='Horobei', force=2, chi=3, honor_requirement=0, personal_honor=3, gold_cost=4, clan=[Unaligned], keywords=[Duelist, Kensai, Ronin, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Myuken = Personality(id=11231, title='Myuken', force=3, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[Unaligned], keywords=[Actor, Ronin, SoulOf('Kyogen')], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yotsu_Shinzai = Personality(id=11232, title='Yotsu Shinzai', force=1, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[Unaligned], keywords=[Shugenja, SoulOf('Yotsu Seiki')], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])