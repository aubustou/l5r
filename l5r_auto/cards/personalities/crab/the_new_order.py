from __future__ import annotations

from l5r_auto.clans import CrabClan, NinjaFaction
from l5r_auto.keywords import (
    Courtier,
    Experienced,
    Imperial,
    Kensai,
    Kolat,
    LordOfBlades,
    LoveLetter,
    Merchant,
    Ninja,
    Samurai,
    Scout,
    Siege,
    Tactician,
    TheMaskedCrab,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(<b>Battle:</b> Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i><br>Courtesy: Ayameko has <b>Resilient</b>. <i>(Courtesy traits do not take effect if you went first. Once per game per card, a Resilient card does not die in battle resolution.)</i>"
Hida_Ayameko = Personality(
    card_id=11884,
    title="Hida Ayameko",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Melee 2 Attack. You may bow one of Kenjiro's Followers or Weapons to straighten him."
Hida_Kenjiro = Personality(
    card_id=11888,
    title="Hida Kenjiro",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Kensai, LordOfBlades, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"While O-Win is opposing a Shadowlands or Spider Clan Personality, his printed ability is <b>Unstoppable</b> and its Fear has +1 strength.<br><b>Battle:</b> Fear 3."
Hida_OWin = Personality(
    card_id=11885,
    title="Hida O-Win",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Toshi enters play for 1 less Gold if you are a Scorpion Clan player."
Hiruma_Toshi = Personality(
    card_id=11886,
    title="Hiruma Toshi",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[CrabClan, NinjaFaction],
    keywords=[Ninja, Samurai, Scout, TheMaskedCrab],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> If Akemi is opposed, show a random card in the enemy leader's hand. You may discard a card with a higher Focus Value <i>(from your hand)</i> to discard the shown card."
Kaiu_Akemi_the_Diplomat = Personality(
    card_id=11887,
    title="Kaiu Akemi, the Diplomat",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Courtier, LoveLetter, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Economic Kolat Open, :bow:, :g5::</b> Draw a card."
Yasuki_Makoto_Imperial_Advisor_Experienced = Personality(
    card_id=11889,
    title="Yasuki Makoto, Imperial Advisor",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Unique, Courtier, Experienced("1"), Imperial, Kolat, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
