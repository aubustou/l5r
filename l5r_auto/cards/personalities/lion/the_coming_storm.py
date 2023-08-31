from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Akodo_Iketsu = Personality(
    id=11746,
    title="Akodo Iketsu",
    force=2,
    chi=3,
    honor_requirement=7,
    personal_honor=3,
    gold_cost=7,
    clan=[LionClan],
    keywords=[Tactician, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Ikoma_Keisuke = Personality(
    id=11747,
    title="Ikoma Keisuke",
    force=3,
    chi=2,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=6,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Ikoma_Shungo = Personality(
    id=11748,
    title="Ikoma Shungo",
    force=2,
    chi=1,
    honor_requirement=7,
    personal_honor=3,
    gold_cost=5,
    clan=[LionClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kitsu_Asato = Personality(
    id=11749,
    title="Kitsu Asato",
    force=2,
    chi=3,
    honor_requirement=7,
    personal_honor=3,
    gold_cost=5,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kitsu_Leiko = Personality(
    id=11750,
    title="Kitsu Leiko",
    force=0,
    chi=3,
    honor_requirement=10,
    personal_honor=3,
    gold_cost=10,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Matsu_Marii = Personality(
    id=11751,
    title="Matsu Marii",
    force=2,
    chi=2,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=4,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
