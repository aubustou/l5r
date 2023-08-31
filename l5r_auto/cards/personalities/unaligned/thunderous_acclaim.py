from __future__ import annotations

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

from ..common import Personality

Ashigaru_Gunso = Personality(
    card_id=12332,
    title="Ashigaru Gunso",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Ashigaru, Commander],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Banished_Experienced = Personality(
    card_id=12333,
    title="Banished",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Resilient, Experienced("1"), Ishiken, Ronin, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Kenturo = Personality(
    card_id=12334,
    title="Kenturo",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Ashigaru, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Seppun_Omihiru = Personality(
    card_id=12335,
    title="Seppun Omihiru",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=2,
    clan=[Unaligned],
    keywords=[Imperial, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Venerable_Spirit = Personality(
    card_id=12336,
    title="Venerable Spirit",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[Unaligned, SpiritFaction],
    keywords=[Ashigaru, Spirit],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
