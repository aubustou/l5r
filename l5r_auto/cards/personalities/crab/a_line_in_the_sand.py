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
