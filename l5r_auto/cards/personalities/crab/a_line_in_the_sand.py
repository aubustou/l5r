from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Hida_Kozan_Voice_of_the_Empress = Personality(
    id=11562,
    title="Hida Kozan, Voice of the Empress",
    force=3,
    chi=3,
    honor_requirement=0,
    personal_honor=3,
    gold_cost=10,
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
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Hida_Kurima = Personality(
    id=11563,
    title="Hida Kurima",
    force=5,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=9,
    clan=[CrabClan],
    keywords=[Conqueror, Resilient, Berserker],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Hiruma_Daizen = Personality(
    id=11564,
    title="Hiruma Daizen",
    force=3,
    chi=1,
    honor_requirement=3,
    personal_honor=3,
    gold_cost=5,
    clan=[CrabClan],
    keywords=[Resilient, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kuni_Araizen = Personality(
    id=11565,
    title="Kuni Araizen",
    force=2,
    chi=3,
    honor_requirement=0,
    personal_honor=1,
    gold_cost=5,
    clan=[CrabClan],
    keywords=[Earth, Jade, Scout, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Yasuki_Hora = Personality(
    id=11566,
    title="Yasuki Hora",
    force=0,
    chi=4,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=5,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Yasuki_Nakura = Personality(
    id=11567,
    title="Yasuki Nakura",
    force=0,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=3,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
