from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Destined,
    Earth,
    Fire,
    Resilient,
    Samurai,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Agasha_Beiru = Personality(
    id=11592,
    title="Agasha Beiru",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Isawa_Kaisei = Personality(
    id=11593,
    title="Isawa Kaisei",
    force=0,
    chi=3,
    personal_honor=4,
    gold_cost=7,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Cavalry, Destined, Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Isawa_Orinoko = Personality(
    id=11594,
    title="Isawa Orinoko",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=None,
    clan=[PhoenixClan],
    keywords=[Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Isawa_Waiko = Personality(
    id=11595,
    title="Isawa Waiko",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Resilient, Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shiba_Tuoko = Personality(
    id=11596,
    title="Shiba Tuoko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Resilient, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shiba_Yinfuo = Personality(
    id=11597,
    title="Shiba Yinfuo",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
