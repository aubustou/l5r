from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Cavalry,
    Commander,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    Tactician,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Akodo_Iketsu = Personality(
    id=11746,
    title="Akodo Iketsu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Tactician, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Ikoma_Keisuke = Personality(
    id=11747,
    title="Ikoma Keisuke",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Ikoma_Shungo = Personality(
    id=11748,
    title="Ikoma Shungo",
    force=2,
    chi=1,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Kitsu_Asato = Personality(
    id=11749,
    title="Kitsu Asato",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Kitsu_Leiko = Personality(
    id=11750,
    title="Kitsu Leiko",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Matsu_Marii = Personality(
    id=11751,
    title="Matsu Marii",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
