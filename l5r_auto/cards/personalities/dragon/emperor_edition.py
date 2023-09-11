from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Earth, Monk, SoulOf, Tattooed, Void
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"Korimi has +2F while defending. <br><b>Interrupt, :bow::</b> After you Recruit Korimi, draw a card."
Togashi_Korimi = Personality(
    card_id=8545,
    title="Togashi Korimi",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Earth, Monk, SoulOf("Togashi Oki"), Tattooed],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
Togashi_Tsukagi = Personality(
    card_id=8591,
    title="Togashi Tsukagi",
    force=4,
    chi=4,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, SoulOf("Togashi Akagi"), Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
