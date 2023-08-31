from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Air, Cavalry, Commander, Conqueror, Courtier, Duelist, Earth, Expendable, Experienced, Imperial, Magistrate, Monk, Mountaineer, Samurai, Shugenja, SoulOf, Tattooed, Unique, Void
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
Kitsuki_Einosuke = Personality(id=12103, title='Kitsuki Einosuke', force=3, chi=2, honor_requirement=5, personal_honor=3, gold_cost=6, clan=[DragonClan], keywords=[Expendable, Courtier, Magistrate], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kitsuki_Goichi = Personality(id=12104, title='Kitsuki Goichi', force=3, chi=4, honor_requirement=5, personal_honor=3, gold_cost=7, clan=[DragonClan], keywords=[Magistrate, Samurai, SoulOf('Kitsuki Berii')], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Kitsuki_Masamitsu = Personality(id=12105, title='Kitsuki Masamitsu', force=2, chi=3, honor_requirement=5, personal_honor=3, gold_cost=6, clan=[DragonClan], keywords=[Air, Courtier, Magistrate, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Mirumoto_Akifumi = Personality(id=12106, title='Mirumoto Akifumi', force=3, chi=3, honor_requirement=2, personal_honor=3, gold_cost=5, clan=[DragonClan], keywords=[Samurai, Void], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Mirumoto_Eisuke = Personality(id=12107, title='Mirumoto Eisuke', force=2, chi=4, honor_requirement=None, personal_honor=3, gold_cost=5, clan=[DragonClan], keywords=[Samurai, SoulOf('Mirumoto Daini')], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Mirumoto_Rikiya = Personality(id=12108, title='Mirumoto Rikiya', force=3, chi=3, honor_requirement=4, personal_honor=2, gold_cost=6, clan=[DragonClan], keywords=[Duelist, Samurai, SoulOf('Mirumoto Washizuka')], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Mirumoto_Tsuda_Emerald_Champion_Experienced = Personality(id=12109, title='Mirumoto Tsuda, Emerald Champion', force=3, chi=5, honor_requirement=8, personal_honor=3, gold_cost=10, clan=[DragonClan], keywords=[Cavalry, Duelist, Unique, Experienced('1'), Imperial, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tamori_Seiken_Experienced = Personality(id=12110, title='Tamori Seiken', force=3, chi=3, honor_requirement=7, personal_honor=3, gold_cost=7, clan=[DragonClan], keywords=[Cavalry, Unique, Commander, Earth, Experienced('1'), Mountaineer, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tamori_Shoko = Personality(id=12111, title='Tamori Shoko', force=2, chi=3, honor_requirement=4, personal_honor=2, gold_cost=5, clan=[DragonClan], keywords=[Commander, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Tamori_Tsunemi = Personality(id=12112, title='Tamori Tsunemi', force=3, chi=2, honor_requirement=0, personal_honor=2, gold_cost=6, clan=[DragonClan], keywords=[Conqueror, Commander, Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])
Togashi_Taiki = Personality(id=12113, title='Togashi Taiki', force=2, chi=2, honor_requirement=0, personal_honor=1, gold_cost=6, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Monk, Tattooed], traits=[], abilities=[], legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition])