from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Earth,
    ElementalMaster,
    Experienced,
    Jade,
    Loyal,
    Magistrate,
    Resilient,
    Shugenja,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Tadaka need not bow for your Kiho or Spell actions.<br><b>Interrupt:</b> Negate an action from another Shugenja or Spell.<br><b>Earth Jade Unstoppable Battle:</b> Tadaka casts Jade Strike. Bow a target card. Destroy it if it is Shadowlands or has no attachments."
Isawa_Tadaka_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12646,
    title="Isawa Tadaka, Seven Thunder",
    force=4,
    chi=5,
    personal_honor=3,
    gold_cost=12,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[
        Experienced("2CW"),
        Loyal,
        Resilient,
        Unique,
        Earth,
        ElementalMaster,
        Jade,
        Magistrate,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
