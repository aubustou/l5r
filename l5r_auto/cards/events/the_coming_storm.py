from __future__ import annotations

from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Event

"<b>Political Battle/Open:</b> Take the Imperial Favor."
Auspicious_Arrival = Event(
    card_id=11709,
    title="Auspicious Arrival",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After a player's Favor action resolves, he loses 2 Honor.<br><b>Open:</b> Put this Event into play. Discard it after your second turn from now begins."
Denial = Event(
    card_id=11710,
    title="Denial",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Economic Open:</b> Target your Holding. After your next turn begins, give it a +1 Gold Production <b>Wealth</b> token."
The_Blessing = Event(
    card_id=11711,
    title="The Blessing",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
