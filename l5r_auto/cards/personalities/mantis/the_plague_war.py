from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Naval, Ningyo, Nonhuman, Shugenja, Thunder
from l5r_auto.legality import (
    CelestialEdition,
    ModernEdition,
    OnyxEdition,
    TwentyFestivalsEdition,
)

from ..common import Personality

"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i> <br><b>Thunder Battle, :g*::</b> Equip a target Spell to Sarassa. You may take an additional action to use one of the Spell's Battle abilities."
Sarassa = Personality(
    card_id=6475,
    title="Sarassa",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Ningyo, Nonhuman, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition],
)
