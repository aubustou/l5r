from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Destined,
    Fallen,
    Kensai,
    Monk,
    Paragon,
    Samurai,
    Shadowlands,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Draw a card after you Recruit a Destined card.)</i><br>After Ryuko enters play, lose 1 Honor.<br><b>Battle, :bow::</b> Melee 2 Attack."
Daigotsu_Ryuko = Personality(
    card_id=10660,
    title="Daigotsu Ryuko",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Destined, Fallen, Paragon, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<i>(Kensai may attach two One-Handed Weapons.)</i><br><b>Home Battle:</b> If Lao-she would be opposed, move him to the current battlefield. <i>(Home actions may be taken from home.)</i>"
Laoshe = Personality(
    card_id=10663,
    title="Lao-she",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        OnyxEdition,
        ModernEdition,
        ModernEdition,
    ],
)
