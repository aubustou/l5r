from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.keywords import (
    ClanChampion,
    Dragon,
    Duelist,
    Experienced,
    Loyal,
    Nonhuman,
    Samurai,
    Shugenja,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Mirumoto_Hitomi_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12642,
    title="Mirumoto Hitomi, Seven Thunder",
    force=5,
    chi=4,
    personal_honor=1,
    gold_cost=10,
    honor_requirement=None,
    clan=[DragonClan],
    keywords=[Duelist, Experienced("2CW"), Loyal, Unique, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Togashi_Yokuni_Kami_Experienced_2CW = Personality(
    card_id=12643,
    title="Togashi Yokuni, Kami",
    force=6,
    chi=6,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=10,
    clan=[DragonClan],
    keywords=[
        Duelist,
        Experienced("2CW"),
        Unique,
        ClanChampion,
        Dragon,
        Nonhuman,
        Samurai,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
