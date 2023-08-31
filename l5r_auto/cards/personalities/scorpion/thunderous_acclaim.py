from __future__ import annotations

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

from ..common import Personality

Bayushi_Chizuken = Personality(
    card_id=12320,
    title="Bayushi Chizuken",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Resilient, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Bayushi_Fuyuko_Experienced = Personality(
    card_id=12321,
    title="Bayushi Fuyuko",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Bayushi_Tenburo = Personality(
    card_id=12322,
    title="Bayushi Tenburo",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shosuro_Kanako = Personality(
    card_id=12323,
    title="Shosuro Kanako",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Resilient, Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shosuro_Wayari = Personality(
    card_id=12324,
    title="Shosuro Wayari",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Soshi_Mumoshi = Personality(
    card_id=12325,
    title="Soshi Mumoshi",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Air, Ninja, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
