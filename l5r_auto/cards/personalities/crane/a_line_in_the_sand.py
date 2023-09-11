from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Duelist,
    Merchant,
    Resilient,
    Samurai,
    Scout,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Invest :g2::</b> You may target a Port, and you may target a different Market. Give each target a +1GP <b>Wealth </b>token."
Daidoji_Hirota = Personality(
    card_id=11568,
    title="Daidoji Hirota",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Invest :g10::</b> Give Natsuki two +1F/+1C <b>Training </b>tokens, and permanently give her Cavalry. This Invest cost cannot be reduced.<br><b>Battle:</b> Target a Personality at any location; if Natsuki has no Training tokens, the target must have assigned to this battlefield. Move the target here. Straighten him if you do not control him."
Daidoji_Natsuki = Personality(
    card_id=11569,
    title="Daidoji Natsuki",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i>"
Daidoji_Takeda = Personality(
    card_id=11570,
    title="Daidoji Takeda",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Ariyoshi enters play for 1 less Gold if your Allegiance is Progressive.<br><b>Political Battle:</b> Show the top card of your Fate Deck. Target an enemy Personality with Chi less than or equal to the card's Focus Value. His controller may choose to move him home. If he doesn't choose this, draw the top card and take an additional action."
Kakita_Ariyoshi = Personality(
    card_id=11571,
    title="Kakita Ariyoshi",
    force=1,
    chi=5,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Artisan, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Interrupt:</b> After you Recruit Mariko, look at the top card of your Dynasty deck. You may put it at the bottom."
Kakita_Mariko = Personality(
    card_id=11572,
    title="Kakita Mariko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=0,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists. Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Shinichi has +1F while you control Kakita Daitsu.<br><b>Battle:</b> Fear 3."
Kakita_Shinichi = Personality(
    card_id=11573,
    title="Kakita Shinichi",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Duelist, Resilient, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
