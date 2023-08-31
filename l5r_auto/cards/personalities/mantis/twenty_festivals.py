from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Air,
    Commander,
    Daimyo,
    Experienced,
    Fire,
    Kensai,
    Magistrate,
    Naval,
    Reserve,
    Samurai,
    Shugenja,
    SoulOf,
    Thunder,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Moshi_Ikako_Experienced = Personality(
    card_id=12128,
    title="Moshi Ikako",
    force=3,
    chi=5,
    personal_honor=3,
    gold_cost=11,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Naval, Reserve, Unique, Air, Daimyo, Experienced("1"), Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Moshi_Karuiko = Personality(
    card_id=12129,
    title="Moshi Karuiko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Shugenja, SoulOf("Moshi Kamiya"), Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tsuruchi_Arayo = Personality(
    card_id=12130,
    title="Tsuruchi Arayo",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Samurai, SoulOf("Tsuruchi Amaya")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Tsuruchi_Jinrai = Personality(
    card_id=12131,
    title="Tsuruchi Jinrai",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Magistrate, Samurai, SoulOf("Tsuruchi Jougo")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Juriken = Personality(
    card_id=12132,
    title="Yoritomo Juriken",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Kuniken = Personality(
    card_id=12133,
    title="Yoritomo Kuniken",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Matsuo_Experienced = Personality(
    card_id=12134,
    title="Yoritomo Matsuo",
    force=4,
    chi=4,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Unique, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Minoro = Personality(
    card_id=12135,
    title="Yoritomo Minoro",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Nintai = Personality(
    card_id=12136,
    title="Yoritomo Nintai",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Saitsuko = Personality(
    card_id=12137,
    title="Yoritomo Saitsuko",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Tsuhime = Personality(
    card_id=12138,
    title="Yoritomo Tsuhime",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[Naval, Magistrate, Samurai, SoulOf("Yoritomo Eriko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Yoritomo_Waito = Personality(
    card_id=12139,
    title="Yoritomo Waito",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Commander, Samurai, SoulOf("Yoritomo Iwata")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
