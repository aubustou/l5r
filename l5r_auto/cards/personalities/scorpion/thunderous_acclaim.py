from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    Air,
    BitterLies,
    Courtier,
    Duelist,
    Experienced,
    Kensai,
    Ninja,
    Resilient,
    Samurai,
    Shugenja,
    Tactician,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Bayushi_Chizuken = Personality(
    id=12320,
    title="Bayushi Chizuken",
    force=2,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[ScorpionClan],
    keywords=[Resilient, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Bayushi_Fuyuko_Experienced = Personality(
    id=12321,
    title="Bayushi Fuyuko",
    force=1,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=6,
    clan=[ScorpionClan],
    keywords=[Courtier, Experienced("1")],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Bayushi_Tenburo = Personality(
    id=12322,
    title="Bayushi Tenburo",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=5,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Shosuro_Kanako = Personality(
    id=12323,
    title="Shosuro Kanako",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=4,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Resilient, Ninja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Shosuro_Wayari = Personality(
    id=12324,
    title="Shosuro Wayari",
    force=4,
    chi=3,
    honor_requirement=0,
    personal_honor=1,
    gold_cost=6,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Soshi_Mumoshi = Personality(
    id=12325,
    title="Soshi Mumoshi",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Air, Ninja, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
