from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Earth, Shugenja, SoulOf
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
Isawa_Nairuko = Personality(id=10242, title='Isawa Nairuko', force=2, chi=3, honor_requirement=2, personal_honor=3, gold_cost=6, clan=[PhoenixClan], keywords=[Earth, Shugenja, SoulOf('Isawa Mariko')], traits=[], abilities=[], legality=[ModernEdition, EmperorEdition, OnyxEdition, TwentyFestivalsEdition])