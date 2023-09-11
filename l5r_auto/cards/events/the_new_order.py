from __future__ import annotations

from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Event

"<b>Interrupt:</b> You may choose a different one of your <i>(legal)</i> Personalities for the action to target instead of the one chosen by another player, now or after he chooses the target."
Devastating_Betrayal = Event(
    card_id=11866,
    title="Devastating Betrayal",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open:</b> Remove your target Personality from the game. Search your Dynasty deck for a Personality with equal or lower Gold Cost and refill this Province with him face-up."
Seclusion = Event(
    card_id=11867,
    title="Seclusion",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
