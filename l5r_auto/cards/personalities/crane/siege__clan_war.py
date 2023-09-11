from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import ClanChampion, Duelist, Experienced, Loyal, Samurai, Unique
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot gain Corruption tokens or Shadowlands. Favor actions may not target Hoturi. Add Hoturi's PH to the FV of his first focused card per duel. After Hoturi is destroyed, gain Honor equal to his Personal Honor.<br><b>Iaijutsu Battle:</b> Hoturi challenges a target enemy Personality. Destroy the loser. If the loser did not focus from his or her hand, the winner draws a card."
Doji_Hoturi_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12641,
    title="Doji Hoturi, Seven Thunder",
    force=5,
    chi=6,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=10,
    clan=[CraneClan],
    keywords=[Duelist, Experienced("2CW"), Loyal, Unique, ClanChampion, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
