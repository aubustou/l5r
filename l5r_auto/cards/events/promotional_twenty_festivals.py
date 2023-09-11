from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Event

"This Event may not have its effects negated or be discarded from play. After a turn begins, if the active player controls seven Seven Thunder Personalities with no Clan Alignments in common, he or she wins the game.<br><b>Open:</b> Put this Event into play."
Victory_of_the_Thunders = Event(
    card_id=12586,
    title="Victory of the Thunders",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
