from __future__ import annotations

from l5r_auto.clans import MantisClan, NagaFaction
from l5r_auto.keywords import (
    Artisan,
    Destined,
    Earth,
    Kensai,
    Magistrate,
    Naga,
    Naval,
    Prophetess,
    Reserve,
    Resilient,
    Samurai,
    Shugenja,
    Thunder,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Kitsune_Narako = Personality(
    card_id=12308,
    title="Kitsune Narako",
    force=0,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Destined, Earth, Prophetess, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Moshi_Kyan = Personality(
    card_id=12309,
    title="Moshi Kyan",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Resilient, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tsuruchi_Akira = Personality(
    card_id=12310,
    title="Tsuruchi Akira",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Kinshikirai = Personality(
    card_id=12311,
    title="Yoritomo Kinshikirai",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Magistrate, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Kyunan = Personality(
    card_id=12312,
    title="Yoritomo Kyunan",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Reserve, Artisan, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Minoko = Personality(
    card_id=12313,
    title="Yoritomo Minoko",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan, NagaFaction],
    keywords=[Kensai, Naga, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
