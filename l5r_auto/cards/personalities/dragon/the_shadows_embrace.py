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

"<i>(Battle: Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i> <br><b>Battle, :bow::</b> If Kasuru is attacking, draw a card. You may discard a card to straighten Kasuru."
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
