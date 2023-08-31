from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import (
    Ashigaru,
    Conqueror,
    Experienced,
    Kensai,
    Monk,
    Naval,
    Nonhuman,
    Oni,
    Resilient,
    Shadowlands,
    Shugenja,
    Unique,
    Water,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Akuma_no_Obake = Personality(
    id=12488,
    title="Akuma no Obake",
    force=4,
    chi=4,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=7,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Keisho = Personality(
    id=12489,
    title="Keisho",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=3,
    clan=[Unaligned],
    keywords=[Resilient, Ashigaru, Shugenja],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Tetsuo_Experienced_2 = Personality(
    id=12490,
    title="Tetsuo",
    force=4,
    chi=4,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=10,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Conqueror, Experienced("2"), Kensai, Unique, Monk],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
The_Crimson_Mountain_Oni = Personality(
    id=12491,
    title="The Crimson Mountain Oni",
    force=7,
    chi=6,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=14,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Resilient, Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Umikaiju = Personality(
    id=12492,
    title="Umikaiju",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Naval, Nonhuman, Oni, Shadowlands, Water],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
