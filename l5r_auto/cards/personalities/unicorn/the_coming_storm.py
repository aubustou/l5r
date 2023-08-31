from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import Cavalry, Courtier, DeathPriest, Expendable, Merchant, Samurai, Shugenja, StableMaster, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Ide_Aragaki = Personality(id=11781, title='Ide Aragaki', force=1, chi=2, honor_requirement=4, personal_honor=2, gold_cost=3, clan=[UnicornClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Ide_Kosaka = Personality(id=11782, title='Ide Kosaka', force=2, chi=2, honor_requirement=4, personal_honor=3, gold_cost=6, clan=[UnicornClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moto_Erdene = Personality(id=11783, title='Moto Erdene', force=2, chi=1, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[UnicornClan], keywords=[Expendable, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moto_Qorin = Personality(id=11784, title='Moto Qorin', force=3, chi=3, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[UnicornClan], keywords=[Cavalry, DeathPriest, Shugenja, Water], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Shinjo_Ajasu_Topaz_Champion = Personality(id=11785, title='Shinjo Ajasu, Topaz Champion', force=2, chi=2, honor_requirement=5, personal_honor=2, gold_cost=5, clan=[UnicornClan], keywords=[Cavalry, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Utaku_Saiken = Personality(id=11786, title='Utaku Saiken', force=0, chi=2, honor_requirement=None, personal_honor=2, gold_cost=2, clan=[UnicornClan], keywords=[Samurai, StableMaster], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])