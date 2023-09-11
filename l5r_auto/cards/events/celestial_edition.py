from __future__ import annotations

from l5r_auto.keywords import Festival, Unique
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    GoldEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Event

"<b>Open:</b> Discard zero to two cards; each other player in turn order may discard a card. Each player then draws as many cards as he discarded."
A_New_Year = Event(
    card_id=59,
    title="A New Year",
    keywords=[Festival],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
"<b>Open:</b> Each player with 21 or more Family Honor loses 5 Honor."
A_Time_for_Action = Event(
    card_id=89,
    title="A Time for Action",
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        CelestialEdition,
        GoldEdition,
        ModernEdition,
    ],
)
'Players have the ability, "Dynasty: If you, this turn, destroyed a Province in battle resolution, put two Rings into play by their own text, and gained 7 Honor, you may discard the Imperial Favor and pay 10 Gold to win the game."<br><b>Open:</b> Put this Event into play.'
Claiming_the_Throne = Event(
    card_id=1400,
    title="Claiming the Throne",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        OnyxEdition,
        TwentyFestivalsEdition,
    ],
)
"This Event may not be discarded from play <i>(though its Open action may be negated normally)</i>. Players need 10 more Honor to win an Honor Victory.<br><b>Political Open:</b> Destroy your rightmost Province. Put this Event into play."
The_New_Order = Event(
    card_id=8235,
    title="The New Order",
    keywords=[Unique],
    traits=[],
    abilities=[],
    legality=[
        TwentyFestivalsEdition,
        CelestialEdition,
        GoldEdition,
        OnyxEdition,
        DiamondEdition,
        ModernEdition,
    ],
)
