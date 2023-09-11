from __future__ import annotations

from l5r_auto.keywords import Kharmic
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Event

"After a player gains Honor, or any of his opponents lose Honor from the rulebook or cards they do not own, give him an equal number of <b>Influence</b> tokens. A player who begins his turn with 50 or more Influence tokens wins the game. This Event will not be discarded from play, nor have its effects prevented. <br><b>Political Open:</b> If no player controls a copy of Political Standoff, put this Event into play."
Political_Standoff = Event(
    card_id=11139,
    title="Political Standoff",
    keywords=[Kharmic],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
