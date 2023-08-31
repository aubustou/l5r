from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan, SpiritFaction
from l5r_auto.keywords import Ancestor, Cavalry, ChildOfProphecy, Commander, Destined, Duelist, Experienced, Hero, LoveLetter, Magistrate, Naval, Paragon, Samurai, Scout, Shugenja, Spirit, Tactician, TheMaskedLion, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Akodo_Raikitsu = Personality(id=11902, title='Akodo Raikitsu', force=2, chi=3, honor_requirement=6, personal_honor=3, gold_cost=6, clan=[LionClan], keywords=[Duelist, Tactician, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Akodo_Yuyama = Personality(id=11905, title='Akodo Yuyama', force=2, chi=2, honor_requirement=6, personal_honor=3, gold_cost=5, clan=[LionClan, SpiritFaction], keywords=[Destined, Ancestor, Samurai, Scout, Spirit, TheMaskedLion], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Ikoma_Ayumi_Experienced = Personality(id=11903, title='Ikoma Ayumi', force=4, chi=3, honor_requirement=0, personal_honor=1, gold_cost=7, clan=[LionClan], keywords=[Cavalry, Naval, Experienced('1'), Hero, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Kitsu_Suzaki = Personality(id=11904, title='Kitsu Suzaki', force=0, chi=4, honor_requirement=7, personal_honor=3, gold_cost=5, clan=[LionClan], keywords=[ChildOfProphecy, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Matsu_Hachiro_Experienced = Personality(id=11906, title='Matsu Hachiro', force=2, chi=3, honor_requirement=10, personal_honor=4, gold_cost=9, clan=[LionClan], keywords=[Cavalry, Commander, Experienced('1'), Paragon, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Matsu_Misato_the_Hatamoto = Personality(id=11907, title='Matsu Misato, the Hatamoto', force=3, chi=3, honor_requirement=7, personal_honor=3, gold_cost=5, clan=[LionClan], keywords=[LoveLetter, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])