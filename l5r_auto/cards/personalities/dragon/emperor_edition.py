from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Earth, Monk, SoulOf, Tattooed, Void
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

Togashi_Korimi = Personality(
    id=8545,
    title="Togashi Korimi",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=5,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Earth, Monk, SoulOf("Togashi Oki"), Tattooed],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition, EmperorEdition],
)
Togashi_Tsukagi = Personality(
    id=8591,
    title="Togashi Tsukagi",
    force=4,
    chi=4,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, SoulOf("Togashi Akagi"), Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, EmperorEdition, OnyxEdition],
)
