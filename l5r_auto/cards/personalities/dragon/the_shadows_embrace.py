from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Monk, Tactician, Tattooed, Void
from l5r_auto.legality import (
    EmperorEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

Togashi_Kasuru = Personality(
    card_id=9821,
    title="Togashi Kasuru",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=0,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Tactician, Monk, Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
