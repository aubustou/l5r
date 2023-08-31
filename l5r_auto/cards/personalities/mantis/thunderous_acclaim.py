from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan, NagaFaction
from l5r_auto.keywords import Artisan, Destined, Earth, Kensai, Magistrate, Naga, Naval, Prophetess, Reserve, Resilient, Samurai, Shugenja, Thunder, Yojimbo
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Kitsune_Narako = Personality(id=12308, title='Kitsune Narako', force=0, chi=2, honor_requirement=0, personal_honor=3, gold_cost=4, clan=[MantisClan], keywords=[Destined, Earth, Prophetess, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Moshi_Kyan = Personality(id=12309, title='Moshi Kyan', force=3, chi=3, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[MantisClan], keywords=[Resilient, Shugenja, Thunder], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tsuruchi_Akira = Personality(id=12310, title='Tsuruchi Akira', force=2, chi=2, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[MantisClan], keywords=[Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Yoritomo_Kinshikirai = Personality(id=12311, title='Yoritomo Kinshikirai', force=3, chi=4, honor_requirement=None, personal_honor=1, gold_cost=6, clan=[MantisClan], keywords=[Naval, Magistrate, Samurai, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Yoritomo_Kyunan = Personality(id=12312, title='Yoritomo Kyunan', force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[MantisClan], keywords=[Kensai, Reserve, Artisan, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Yoritomo_Minoko = Personality(id=12313, title='Yoritomo Minoko', force=3, chi=2, honor_requirement=None, personal_honor=2, gold_cost=7, clan=[MantisClan, NagaFaction], keywords=[Kensai, Naga, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])