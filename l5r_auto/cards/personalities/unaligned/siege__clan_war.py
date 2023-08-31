from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, Unaligned
from l5r_auto.keywords import (
    Ashigaru,
    Duelist,
    Experienced,
    Monk,
    Ronin,
    Samurai,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

The_Hooded_Ronin_Descendant_of_Shinsei_ExperiencedCW = Personality(
    id=12648,
    title="The Hooded Ronin, Descendant of Shinsei",
    force=2,
    chi=5,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=8,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Duelist, Unique, Ashigaru, Experienced("1"), Monk, Ronin, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, ModernEdition, OnyxEdition],
)
