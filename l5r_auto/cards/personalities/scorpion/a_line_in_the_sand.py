from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Conqueror,
    Courtier,
    Ninja,
    Reserve,
    Resilient,
    Samurai,
    Scout,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Bayushi_Atsuto = Personality(
    id=11598,
    title="Bayushi Atsuto",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Conqueror, Courtier, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Bayushi_Yasunari = Personality(
    id=11599,
    title="Bayushi Yasunari",
    force=3,
    chi=1,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shosuro_Kiyofumi = Personality(
    id=11600,
    title="Shosuro Kiyofumi",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Resilient, Ninja, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shosuro_Yasumasa = Personality(
    id=11601,
    title="Shosuro Yasumasa",
    force=1,
    chi=4,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Soshi_Kitaiko = Personality(
    id=11602,
    title="Soshi Kitaiko",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Courtier, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Yogo_Gingo = Personality(
    id=11603,
    title="Yogo Gingo",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Cavalry, Reserve, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
