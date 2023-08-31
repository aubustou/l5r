from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan, ShadowlandsFaction
from l5r_auto.keywords import (
    Air,
    BitterLies,
    Courtier,
    Duelist,
    Expendable,
    Experienced,
    Kensai,
    Kuroiban,
    Magistrate,
    Ninja,
    Resilient,
    Samurai,
    Shadowlands,
    Shugenja,
    Spy,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Bayushi_Chiyoda = Personality(
    id=12476,
    title="Bayushi Chiyoda",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, ShadowlandsFaction],
    keywords=[Kensai, BitterLies, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Bayushi_Kanihime = Personality(
    id=12477,
    title="Bayushi Kanihime",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Resilient, Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Bayushi_Shenlao = Personality(
    id=12478,
    title="Bayushi Shen-lao",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, Resilient, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shosuro_Kayo_Experienced = Personality(
    id=12479,
    title="Shosuro Kayo",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Experienced("1"), Ninja, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shosuro_Ozu = Personality(
    id=12480,
    title="Shosuro Ozu",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=2,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Expendable, Ninja, Spy],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yogo_Mizoguchi = Personality(
    id=12481,
    title="Yogo Mizoguchi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Courtier, Kuroiban, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
