from __future__ import annotations

from l5r_auto.keywords import GeishaHouse, Port, Temple
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

"Reduce by 1 all Honor gains during the Action Phase for players without Personalities in play.<br>:bow:: Produce 1 Gold. <br><b>Political Limited, :bow::</b> Target a dishonorable Personality. His controller loses Honor equal to his printed Personal Honor or 2, whichever is lower."
Brilliant_Cascade_Inn = Holding(
    card_id=11140,
    title="Brilliant Cascade Inn",
    gold_cost=1,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 1 Gold. <br><b>:bow::</b> When paying for a Holding, it enters play for 2 less Gold."
Deep_Harbor = Holding(
    card_id=11141,
    title="Deep Harbor",
    gold_cost=1,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
":bow:: Produce 1 Gold. <br><b>Limited:</b> If you have not lost Honor from cards you own this game and your Family Honor is below your starting Honor, gain 1 Honor."
Secluded_Shrine = Holding(
    card_id=11144,
    title="Secluded Shrine",
    gold_cost=1,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
