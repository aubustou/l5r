from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Cavalry,
    Conqueror,
    Courtier,
    Duelist,
    Kensai,
    LoveLetter,
    Magistrate,
    Orator,
    Samurai,
    ScourgeOfDarkness,
    Scout,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Daidoji_Nozomi = Personality(
    id=11891,
    title="Daidoji Nozomi",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Cavalry, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Daidoji_Tomomi = Personality(
    id=11890,
    title="Daidoji Tomomi",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Conqueror, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Daidoji_Yurei = Personality(
    id=11895,
    title="Daidoji Yurei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=9,
    clan=[CraneClan],
    keywords=[Duelist, Samurai, ScourgeOfDarkness],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Doji_Shimada = Personality(
    id=11893,
    title="Doji Shimada",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Doji_Takato_the_Manipulator = Personality(
    id=11892,
    title="Doji Takato, the Manipulator",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, LoveLetter, Orator],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kakita_Daitsu = Personality(
    id=11894,
    title="Kakita Daitsu",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Duelist, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
