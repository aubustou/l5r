from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import Air, BitterLies, Bloodspeaker, Commander, Courtier, Experienced, Kensai, LoveLetter, Loyal, Magistrate, Martyr, Musician, Paragon, Samurai, Shugenja, TheMaskedMonkey, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Bayushi_Aggushi_Bayushi_Janqu = Personality(id=11920, title='Bayushi Aggushi & Bayushi Janqu', force=4, chi=3, honor_requirement=0, personal_honor=2, gold_cost=8, clan=[ScorpionClan], keywords=[Courtier, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_Irezu_Experienced = Personality(id=11921, title='Bayushi Irezu', force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[ScorpionClan], keywords=[Kensai, BitterLies, Commander, Experienced('1'), Martyr], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Bayushi_Iyashi_Lady_Sorrow = Personality(id=11922, title='Bayushi Iyashi, Lady Sorrow', force=3, chi=2, honor_requirement=0, personal_honor=3, gold_cost=6, clan=[ScorpionClan], keywords=[Loyal, Magistrate, Musician, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shosuro_Yamazaki_the_Master_Courtier = Personality(id=11923, title='Shosuro Yamazaki, the Master Courtier', force=0, chi=3, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[ScorpionClan], keywords=[Courtier, LoveLetter], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yogo_Chijin = Personality(id=11924, title='Yogo Chijin', force=0, chi=4, honor_requirement=None, personal_honor=0, gold_cost=5, clan=[ScorpionClan], keywords=[Air, Bloodspeaker, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yogo_Gorobei = Personality(id=11925, title='Yogo Gorobei', force=2, chi=2, honor_requirement=None, personal_honor=0, gold_cost=4, clan=[ScorpionClan], keywords=[Magistrate, Samurai, TheMaskedMonkey, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])