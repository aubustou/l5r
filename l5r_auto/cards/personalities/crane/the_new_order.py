from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Daidoji_Nozomi = Personality(
    id=11891,
    title="Daidoji Nozomi",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=7,
    clan=[CraneClan],
    keywords=[Cavalry, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Tomomi = Personality(
    id=11890,
    title="Daidoji Tomomi",
    force=4,
    chi=3,
    honor_requirement=5,
    personal_honor=2,
    gold_cost=8,
    clan=[CraneClan],
    keywords=[Conqueror, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Yurei = Personality(
    id=11895,
    title="Daidoji Yurei",
    force=2,
    chi=3,
    honor_requirement=9,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Duelist, Samurai, ScourgeOfDarkness],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Shimada = Personality(
    id=11893,
    title="Doji Shimada",
    force=2,
    chi=3,
    honor_requirement=2,
    personal_honor=3,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Takato_the_Manipulator = Personality(
    id=11892,
    title="Doji Takato, the Manipulator",
    force=0,
    chi=4,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Courtier, LoveLetter, Orator],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Daitsu = Personality(
    id=11894,
    title="Kakita Daitsu",
    force=3,
    chi=2,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=7,
    clan=[CraneClan],
    keywords=[Duelist, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
