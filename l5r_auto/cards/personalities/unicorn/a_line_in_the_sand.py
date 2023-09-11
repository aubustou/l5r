from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Bully,
    Cavalry,
    Courtier,
    DeathPriest,
    Destined,
    Kensai,
    Merchant,
    Resilient,
    Samurai,
    Shugenja,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Interrupt:</b> After you Recruit Ryou, give a target Holding a +1GP <b>Wealth</b> token.<br><b>Invest :g10::</b> Give <i>(in total)</i> three +1GP Wealth tokens to one to three target Holdings. This Invest cost cannot be reduced."
Ide_Ryou = Personality(
    card_id=11616,
    title="Ide Ryou",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Water Battle:</b> Discard a card from your hand to create Fear equal to the card's Focus Value, +1 if its target is Phoenix Clan."
Iuchi_Kalsang = Personality(
    card_id=11617,
    title="Iuchi Kalsang",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=2,
    clan=[UnicornClan],
    keywords=[Cavalry, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Water Interrupt:</b> The action's Fear effects have +1 strength, may target Items, and destroy attachments after they bow."
Moto_Alani = Personality(
    card_id=11618,
    title="Moto Alani",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Destined, Resilient, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br>Cannot attach Followers.<br><b>Battle:</b> Move your target Infantry Personality at any location to Kyouaku-Inu's battlefield."
Moto_KyouakuInu = Personality(
    card_id=11619,
    title="Moto Kyouaku-Inu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Battle:</b> Melee 2 Attack. If this destroyed a card, you may make a Fear 3 targeting a <i>(legal)</i> card in the same unit."
Shinjo_Shimikoto = Personality(
    card_id=11620,
    title="Shinjo Shimikoto",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Resilient, Bully, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Kimiono enters play for 1 less Gold if your Allegiance is Progressive.<br><b>Political Battle:</b> Fear equal to Kimiono's Personal Honor. If this bowed a card in a unit whose Personality has <b>lower</b> Personal Honor, gain 1 Honor."
Utaku_Kimiono = Personality(
    card_id=11621,
    title="Utaku Kimiono",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
