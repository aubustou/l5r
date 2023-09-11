from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Commander,
    Conqueror,
    Kensai,
    Monk,
    OrderOfTheSpider,
    Samurai,
    Shadowlands,
    SoulOf,
)
from l5r_auto.legality import (
    EmperorEdition,
    IvoryEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(A Conqueror's unit doesn't bow after battle.)</i>"
Daigotsu_Kendo = Personality(
    card_id=1736,
    title="Daigotsu Kendo",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Conqueror, Commander, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br><b>Battle/Open:</b> Straighten a target Personality with a Weapon."
Sandayu = Personality(
    card_id=6467,
    title="Sandayu",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk, OrderOfTheSpider, SoulOf("Torao")],
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
