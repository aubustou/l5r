from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Ninja
from l5r_auto.legality import (
    EmperorEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"After Kodanshi enters play from a Province, create a 0F/2C/0PH Ninja Scorpion Clan Personality."
Soshi_Kodanshi = Personality(
    card_id=10082,
    title="Soshi Kodanshi",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
