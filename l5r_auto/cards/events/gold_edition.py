from __future__ import annotations

from l5r_auto.legality import (
    GoldEdition,
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"You do not pay the extra two Gold for bringing Personalities with the named Clan Alignment into play.<br><b>Open:</b> Put this Event into play. Name a Clan Alignment other than your own."
Alliance = Event(
    card_id=331,
    title="Alliance",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
    ],
)
"<b>Dynasty:</b> Draw a card. <i>(You may only take Dynasty actions during your Dynasty Phase.)</i>"
Glimpse_of_the_Unicorn = Event(
    card_id=2818,
    title="Glimpse of the Unicorn",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        ImperialEdition,
        GoldEdition,
        JadeEdition,
        ModernEdition,
        ModernEdition,
    ],
)
