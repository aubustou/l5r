from __future__ import annotations

from l5r_auto.clans import MantisClan, ShadowlandsFaction
from l5r_auto.keywords import (
    Air,
    BountyHunter,
    Destined,
    Experienced,
    Fire,
    Kensai,
    Magistrate,
    Mercenary,
    Naval,
    Samurai,
    Scout,
    Shadowlands,
    Shugenja,
    Thunder,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Moshi_Chiyoko = Personality(
    id=12464,
    title="Moshi Chiyoko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Fire, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Moshi_Nariko = Personality(
    id=12465,
    title="Moshi Nariko",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Air, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tsuruchi_Kinuyo = Personality(
    id=12466,
    title="Tsuruchi Kinuyo",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Destined, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tsuruchi_Taito_Experienced = Personality(
    id=12467,
    title="Tsuruchi Taito",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, BountyHunter, Experienced("1"), Magistrate, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Honjo = Personality(
    id=12468,
    title="Yoritomo Honjo",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Tamiya = Personality(
    id=12469,
    title="Yoritomo Tamiya",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan, ShadowlandsFaction],
    keywords=[Kensai, Naval, Mercenary, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
