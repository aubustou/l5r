from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import SpiritFaction, Unaligned
from l5r_auto.keywords import (
    Ashigaru,
    Commander,
    Experienced,
    Imperial,
    Ishiken,
    Magistrate,
    Resilient,
    Ronin,
    Scout,
    Shugenja,
    Spirit,
    Void,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

Ashigaru_Gunso = Personality(
    id=12332,
    title="Ashigaru Gunso",
    force=2,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=7,
    clan=[Unaligned],
    keywords=[Ashigaru, Commander],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
Banished_Experienced = Personality(
    id=12333,
    title="Banished",
    force=3,
    chi=4,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=7,
    clan=[Unaligned],
    keywords=[Resilient, Experienced("1"), Ishiken, Ronin, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
Kenturo = Personality(
    id=12334,
    title="Kenturo",
    force=2,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=6,
    clan=[Unaligned],
    keywords=[Ashigaru, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
Seppun_Omihiru = Personality(
    id=12335,
    title="Seppun Omihiru",
    force=3,
    chi=3,
    honor_requirement=2,
    personal_honor=3,
    gold_cost=5,
    clan=[Unaligned],
    keywords=[Imperial, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
Venerable_Spirit = Personality(
    id=12336,
    title="Venerable Spirit",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=5,
    clan=[Unaligned, SpiritFaction],
    keywords=[Ashigaru, Spirit],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
