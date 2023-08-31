from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Earth,
    Kensai,
    Merchant,
    Naval,
    Nonhuman,
    Resilient,
    Samurai,
    Scout,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Kitsune_Nakumi = Personality(
    card_id=11586,
    title="Kitsune Nakumi",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Earth, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kitsune_Satoko = Personality(
    card_id=11587,
    title="Kitsune Satoko",
    force=0,
    chi=4,
    personal_honor=4,
    gold_cost=5,
    honor_requirement=6,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tsuruchi_Kaitaru = Personality(
    card_id=11588,
    title="Tsuruchi Kaitaru",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Naval, Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tsuruchi_Taito = Personality(
    card_id=11589,
    title="Tsuruchi Taito",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Dairu = Personality(
    card_id=11590,
    title="Yoritomo Dairu",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Artisan, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Haruna = Personality(
    card_id=11591,
    title="Yoritomo Haruna",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
