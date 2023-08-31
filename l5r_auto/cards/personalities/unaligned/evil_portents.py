from __future__ import annotations

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

from ..common import Personality

Akuma_no_Obake = Personality(
    id=12488,
    title="Akuma no Obake",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Keisho = Personality(
    id=12489,
    title="Keisho",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Resilient, Ashigaru, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tetsuo_Experienced_2 = Personality(
    id=12490,
    title="Tetsuo",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=10,
    honor_requirement=None,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Conqueror, Experienced("2"), Kensai, Unique, Monk],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Crimson_Mountain_Oni = Personality(
    id=12491,
    title="The Crimson Mountain Oni",
    force=7,
    chi=6,
    personal_honor=0,
    gold_cost=14,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Resilient, Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Umikaiju = Personality(
    id=12492,
    title="Umikaiju",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Naval, Nonhuman, Oni, Shadowlands, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
