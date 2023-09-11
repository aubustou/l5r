from __future__ import annotations

from l5r_auto.keywords import Unique
from l5r_auto.legality import (
    ImperialEdition,
    IvoryEdition,
    LotusEdition,
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"Each player may draw an additional card before his turn ends if he Equipped any Followers from his hand since his last turn ended.<br><b>Open:</b> Put this Event into play."
Enlistment = Event(
    card_id=2346,
    title="Enlistment",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        LotusEdition,
        ImperialEdition,
        OnyxEdition,
        SamuraiEdition,
        ModernEdition,
    ],
)
'You cannot win an Honor Victory or control the Imperial Favor. You have the ability, "<b>Repeatable Interrupt:</b> Negate a Favor action after it targets your cards <i>(the Imperial Favor is still discarded)</i>. Lose 5 Honor."<br><b>Open:</b> Put this Event into play. Discard the Imperial Favor if you control it.'
Severed_from_the_Emperor = Event(
    card_id=6636,
    title="Severed from the Emperor",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        LotusEdition,
        ImperialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
