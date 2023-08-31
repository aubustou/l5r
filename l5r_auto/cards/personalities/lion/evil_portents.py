from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Beastmaster, Cavalry, Commander, Duelist, Experienced, Paragon, Samurai, ScionOfTheWind, Scout, Tactician
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Akodo_Misaka = Personality(id=12458, title='Akodo Misaka', force=3, chi=3, honor_requirement=7, personal_honor=3, gold_cost=6, clan=[LionClan], keywords=[Duelist, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Ikoma_Morita = Personality(id=12459, title='Ikoma Morita', force=2, chi=2, honor_requirement=4, personal_honor=2, gold_cost=5, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Matsu_Akio = Personality(id=12460, title='Matsu Akio', force=3, chi=2, honor_requirement=6, personal_honor=2, gold_cost=5, clan=[LionClan], keywords=[Duelist, Tactician, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Matsu_Takeuchi = Personality(id=12461, title='Matsu Takeuchi', force=3, chi=3, honor_requirement=6, personal_honor=3, gold_cost=6, clan=[LionClan], keywords=[Cavalry, Beastmaster, Commander, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Matsu_Tayuko_Experienced = Personality(id=12462, title='Matsu Tayuko', force=1, chi=3, honor_requirement=8, personal_honor=3, gold_cost=5, clan=[LionClan], keywords=[Experienced('1'), Paragon, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Matsu_Yamamura = Personality(id=12463, title='Matsu Yamamura', force=1, chi=3, honor_requirement=4, personal_honor=2, gold_cost=3, clan=[LionClan], keywords=[Beastmaster, Commander, Samurai, ScionOfTheWind], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])