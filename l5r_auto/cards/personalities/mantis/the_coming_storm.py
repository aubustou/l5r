from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Earth, Experienced, Jade, Kolat, LadyOfTheSun, Magistrate, Naval, Reserve, Samurai, Scout, Shugenja, Thunder, Unique
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Kitsune_Beiko = Personality(id=11752, title='Kitsune Beiko', force=0, chi=1, honor_requirement=2, personal_honor=3, gold_cost=10, clan=[MantisClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Moshi_Raiko = Personality(id=11753, title='Moshi Raiko', force=2, chi=2, honor_requirement=0, personal_honor=2, gold_cost=4, clan=[MantisClan], keywords=[Naval, LadyOfTheSun, Shugenja, Thunder], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Tsuruchi_Hikari = Personality(id=11754, title='Tsuruchi Hikari', force=2, chi=1, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[MantisClan], keywords=[Reserve, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Tsuruchi_Yashiro_Defender_of_the_Obsidian_Blades_Experienced = Personality(id=11755, title='Tsuruchi Yashiro, Defender of the Obsidian Blades', force=3, chi=2, honor_requirement=None, personal_honor=2, gold_cost=7, clan=[MantisClan], keywords=[Unique, Experienced('1'), Jade, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yoritomo_Shotsuo = Personality(id=11756, title='Yoritomo Shotsuo', force=3, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[MantisClan], keywords=[Naval, Samurai, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Yoritomo_Yusuke = Personality(id=11757, title='Yoritomo Yusuke', force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[MantisClan], keywords=[Kolat, Magistrate, Samurai], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])