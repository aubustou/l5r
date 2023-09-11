from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    Conqueror,
    Courtier,
    Earth,
    Imperial,
    Jade,
    Magistrate,
    Merchant,
    Resilient,
    Samurai,
    Scout,
    Shugenja,
    Unique,
    VoiceOfTheEmpress,
    Void,
    WitchHunter,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Kozan enters play for 1 less Gold if your Allegiance is Traditionalist. Kozan need not bow to Lobby. After you Recruit Kozan, take the Imperial Favor. You have a Lobby Bonus of three times Kozan's Personal Honor.<br><b>Favor Political Battle/Open:</b> Discard the Imperial Favor to bow a target Personality."
Hida_Kozan_Voice_of_the_Empress = Personality(
    card_id=11562,
    title="Hida Kozan, Voice of the Empress",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[
        Unique,
        Earth,
        Imperial,
        Magistrate,
        Shugenja,
        VoiceOfTheEmpress,
        Void,
        WitchHunter,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle. Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Cannot attach Items."
Hida_Kurima = Personality(
    card_id=11563,
    title="Hida Kurima",
    force=5,
    chi=2,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Conqueror, Resilient, Berserker],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Daizen has <b>Naval</b> while you control a Port."
Hiruma_Daizen = Personality(
    card_id=11564,
    title="Hiruma Daizen",
    force=3,
    chi=1,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Earth Battle:</b> Bow Araizen's target unbowed Follower or Spell to make a Melee Attack equal to Araizen's Chi."
Kuni_Araizen = Personality(
    card_id=11565,
    title="Kuni Araizen",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Earth, Jade, Scout, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Invest :g10::</b> Put one or two target Economic Strategies in your discard pile into your hand, and bow Hora. This Invest cost cannot be reduced.<br><b>Economic Open, :bow::</b> Increase or decrease a target Holding's Gold Production <i>(this turn)</i> by half Hora's Chi, rounded up."
Yasuki_Hora = Personality(
    card_id=11566,
    title="Yasuki Hora",
    force=0,
    chi=4,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce Gold equal to Nakura's Chi that can only pay for a single Economic action."
Yasuki_Nakura = Personality(
    card_id=11567,
    title="Yasuki Nakura",
    force=0,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
