from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import Cavalry, Commander, Conqueror, Courtier, DeathPriest, Hatamoto, Magistrate, Merchant, Samurai, ScionOfTheVoid, Shugenja, Void, Water, Zealot
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Ide_Hideshi_Topaz_Champion = Personality(id=11938, title='Ide Hideshi, Topaz Champion', force=2, chi=3, honor_requirement=0, personal_honor=3, gold_cost=6, clan=[UnicornClan], keywords=[Cavalry, Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Ide_Igo = Personality(id=11939, title='Ide Igo', force=1, chi=3, honor_requirement=4, personal_honor=3, gold_cost=4, clan=[UnicornClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moto_Chizura = Personality(id=11942, title='Moto Chizura', force=3, chi=3, honor_requirement=None, personal_honor=0, gold_cost=6, clan=[UnicornClan], keywords=[Conqueror, DeathPriest, Hatamoto, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moto_Nergui = Personality(id=11940, title='Moto Nergui', force=2, chi=4, honor_requirement=None, personal_honor=0, gold_cost=6, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, ScionOfTheVoid, Shugenja, Void, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moto_Tadasu = Personality(id=11941, title='Moto Tadasu', force=3, chi=2, honor_requirement=0, personal_honor=1, gold_cost=8, clan=[UnicornClan], keywords=[Cavalry, Commander, Samurai, Zealot], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shinjo_Saeki = Personality(id=11943, title='Shinjo Saeki', force=2, chi=3, honor_requirement=3, personal_honor=3, gold_cost=6, clan=[UnicornClan], keywords=[Cavalry, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])