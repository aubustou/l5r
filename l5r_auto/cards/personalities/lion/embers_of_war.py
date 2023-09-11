from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import Shugenja, SodanSenzo, Water
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<b>Home Battle, :bow::</b> Create a 2F/2C/3PH Lion <b>Clan &#149; Ancestor &#149; Samurai &#149; Spirit</b> Personality at the current battlefield. Remove him from the game after the battle ends. <i>(Home actions can be taken from home.)</i>"
Kitsu_Miro = Personality(
    card_id=4386,
    title="Kitsu Miro",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Shugenja, SodanSenzo, Water],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
