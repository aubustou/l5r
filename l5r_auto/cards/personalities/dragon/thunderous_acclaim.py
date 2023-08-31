from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Commander, Courtier, Duelist, Earth, Expendable, Experienced, Fire, Kensai, Magistrate, Monk, Resilient, Samurai, Shugenja, Tactician, Tattooed
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Kitsuki_Akito = Personality(id=12296, title='Kitsuki Akito', force=1, chi=1, honor_requirement=4, personal_honor=3, gold_cost=4, clan=[DragonClan], keywords=[Expendable, Courtier, Magistrate], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kitsuki_Mizukabe = Personality(id=12297, title='Kitsuki Mizukabe', force=3, chi=4, honor_requirement=7, personal_honor=3, gold_cost=7, clan=[DragonClan], keywords=[Resilient, Courtier, Magistrate], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Mirumoto_Higaru_Experienced = Personality(id=12298, title='Mirumoto Higaru', force=4, chi=3, honor_requirement=4, personal_honor=2, gold_cost=7, clan=[DragonClan], keywords=[Duelist, Kensai, Experienced('1'), Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tamori_Hirakura = Personality(id=12299, title='Tamori Hirakura', force=3, chi=2, honor_requirement=0, personal_honor=2, gold_cost=6, clan=[DragonClan], keywords=[Resilient, Commander, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tamori_Mabasu = Personality(id=12300, title='Tamori Mabasu', force=2, chi=2, honor_requirement=3, personal_honor=1, gold_cost=5, clan=[DragonClan], keywords=[Tactician, Commander, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Togashi_Tameko = Personality(id=12301, title='Togashi Tameko', force=0, chi=2, honor_requirement=4, personal_honor=2, gold_cost=4, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Fire, Monk, Tattooed], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])