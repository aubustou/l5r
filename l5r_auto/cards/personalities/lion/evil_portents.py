from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Cavalry,
    Commander,
    Duelist,
    Experienced,
    Paragon,
    Samurai,
    ScionOfTheWind,
    Scout,
    Tactician,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Akodo_Misaka = Personality(
    id=12458,
    title="Akodo Misaka",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Ikoma_Morita = Personality(
    id=12459,
    title="Ikoma Morita",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Akio = Personality(
    id=12460,
    title="Matsu Akio",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Duelist, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Takeuchi = Personality(
    id=12461,
    title="Matsu Takeuchi",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Cavalry, Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Tayuko_Experienced = Personality(
    id=12462,
    title="Matsu Tayuko",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=8,
    clan=[LionClan],
    keywords=[Experienced("1"), Paragon, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Yamamura = Personality(
    id=12463,
    title="Matsu Yamamura",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai, ScionOfTheWind],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
