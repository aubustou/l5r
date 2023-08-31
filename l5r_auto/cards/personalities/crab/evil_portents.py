from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Commander,
    Daimyo,
    Earth,
    Experienced,
    Jade,
    Loyal,
    Magistrate,
    Reserve,
    Resilient,
    Samurai,
    Shugenja,
    Siege,
    Tactician,
    Unique,
    WitchHunter,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Hida_Genda = Personality(
    id=12440,
    title="Hida Genda",
    force=4,
    chi=2,
    honor_requirement=0,
    personal_honor=1,
    gold_cost=9,
    clan=[CrabClan],
    keywords=[Tactician, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kaiu_Eichi = Personality(
    id=12441,
    title="Kaiu Eichi",
    force=3,
    chi=4,
    honor_requirement=3,
    personal_honor=3,
    gold_cost=6,
    clan=[CrabClan],
    keywords=[Resilient, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kaiu_OTaro = Personality(
    id=12442,
    title="Kaiu O-Taro",
    force=4,
    chi=2,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=7,
    clan=[CrabClan],
    keywords=[Reserve, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kuni_Hokinsha = Personality(
    id=12443,
    title="Kuni Hokinsha",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=4,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kuni_Renyu_Experienced_4 = Personality(
    id=12444,
    title="Kuni Renyu",
    force=5,
    chi=5,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=12,
    clan=[CrabClan],
    keywords=[
        Experienced("4"),
        Loyal,
        Unique,
        Daimyo,
        Earth,
        Jade,
        Magistrate,
        Shugenja,
        WitchHunter,
    ],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Kuni_Tenba = Personality(
    id=12445,
    title="Kuni Tenba",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=6,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)