from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Earth,
    Kensai,
    Merchant,
    Naval,
    Nonhuman,
    Resilient,
    Samurai,
    Scout,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Interrupt:</b> After you Recruit Nakumi, create a 1F/2C/3PH <b>Mantis Clan &#149; Fox &#149; Nonhuman &#149; Spirit &#149; Resilient</b> Personality. <i>(Once per game per card, a Resilient card does not die in battle resolution.)</i>"
Kitsune_Nakumi = Personality(
    card_id=11586,
    title="Kitsune Nakumi",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Earth, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Satoko enters play for 1 less Gold if your Allegiance is Progressive.<br><b>Home Battle, :bow::</b> Move your target Spirit Personality home. You may rehonor it."
Kitsune_Satoko = Personality(
    card_id=11587,
    title="Kitsune Satoko",
    force=0,
    chi=4,
    personal_honor=4,
    gold_cost=5,
    honor_requirement=6,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Invest :g10:: Produce 15 Gold. This Invest cost cannot be reduced."
Tsuruchi_Kaitaru = Personality(
    card_id=11588,
    title="Tsuruchi Kaitaru",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Naval, Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack. If the Defender has not had an opportunity to take a Battle action or pass, discard a card."
Tsuruchi_Taito = Personality(
    card_id=11589,
    title="Tsuruchi Taito",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br><b>Battle:</b> Bow a target enemy attachment with lower Force. You may bow one of Dairu's Weapons or one of your Ports to destroy the target."
Yoritomo_Dairu = Personality(
    card_id=11590,
    title="Yoritomo Dairu",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Artisan, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Economic Open, :bow::</b> Target a Market or Port card in your Province. You may either take an additional action to use one of its abilities ignoring bow costs, produce 2 Gold, or target your Personality and give him +2F, or +3F if he is Spider Clan. Discard the card and refill the Province face-up."
Yoritomo_Haruna = Personality(
    card_id=11591,
    title="Yoritomo Haruna",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
