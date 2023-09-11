from __future__ import annotations

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

from ..common import Personality

"Cannot gain Corruption tokens or Shadowlands. Can only be controlled by his owner. Need not bow for your Kiho actions.<br><b>Open, :bow:, :gstar::</b> Give <b>Destined</b> to a target face-up Personality in a Province and ignore their Honor Requirement. If they are a Seven Thunder, you may Recruit them. One or more target players may each straighten a Ring they control."
The_Hooded_Ronin_Descendant_of_Shinsei_ExperiencedCW = Personality(
    card_id=12648,
    title="The Hooded Ronin, Descendant of Shinsei",
    force=2,
    chi=5,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=0,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Duelist, Unique, Ashigaru, Experienced("1"), Monk, Ronin, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
