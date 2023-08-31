from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Destined,
    Earth,
    Experienced,
    Jade,
    Resilient,
    Samurai,
    Shugenja,
    Siege,
    TheMaskedTortoise,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Hida_Toranosuke_Experienced = Personality(
    id=12284,
    title="Hida Toranosuke",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Resilient, Experienced("1"), Jade, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kaiu_Gizen = Personality(
    id=12285,
    title="Kaiu Gizen",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=2,
    clan=[CrabClan],
    keywords=[Destined, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kaiu_Otogou = Personality(
    id=12286,
    title="Kaiu Otogou",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kuni_Igarasu = Personality(
    id=12287,
    title="Kuni Igarasu",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=3,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kuni_Soseki = Personality(
    id=12288,
    title="Kuni Soseki",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Resilient, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Toritaka_Suppon = Personality(
    id=12289,
    title="Toritaka Suppon",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=2,
    clan=[CrabClan],
    keywords=[Samurai, TheMaskedTortoise],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
