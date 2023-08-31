from __future__ import annotations

from l5r_auto.keywords import Kharmic
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Event

Political_Standoff = Event(
    card_id=11139,
    title="Political Standoff",
    keywords=[Kharmic],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
