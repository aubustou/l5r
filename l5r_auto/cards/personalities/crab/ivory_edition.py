from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Berserker,
    ClanChampion,
    Earth,
    Engineer,
    Experienced,
    Kensai,
    Loyal,
    Samurai,
    Scout,
    Shugenja,
    Siege,
    SoulOf,
    Tactician,
    TheLittleBear,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Hida_Ayahi = Personality(
    id=11145,
    title="Hida Ayahi",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Berserker, Samurai, SoulOf("Hida Kashin")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hida_Kisada_the_Little_Bear_Experienced = Personality(
    id=11146,
    title="Hida Kisada, the Little Bear",
    force=5,
    chi=5,
    personal_honor=3,
    gold_cost=12,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[
        Kensai,
        Loyal,
        Tactician,
        Unique,
        ClanChampion,
        Experienced("1"),
        Samurai,
        Siege,
        TheLittleBear,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hida_Reigoro = Personality(
    id=11147,
    title="Hida Reigoro",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Samurai, SoulOf("Hida Renga")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hida_Saiyuki = Personality(
    id=11148,
    title="Hida Saiyuki",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Samurai, SoulOf("Kaiu Hisayuki")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hida_Toranosuke = Personality(
    id=11149,
    title="Hida Toranosuke",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hiruma_Fujito = Personality(
    id=11150,
    title="Hiruma Fujito",
    force=2,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hiruma_Itta = Personality(
    id=11151,
    title="Hiruma Itta",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[CrabClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hiruma_Tsurao = Personality(
    id=11152,
    title="Hiruma Tsurao",
    force=2,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Scout, SoulOf("Hiruma Todori")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kaiu_Nakagawa = Personality(
    id=11153,
    title="Kaiu Nakagawa",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=5,
    clan=[CrabClan],
    keywords=[Engineer, Samurai, Siege, SoulOf("Kaiu Shoichi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kuni_Tomokazu = Personality(
    id=11154,
    title="Kuni Tomokazu",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Earth, Shugenja, SoulOf("Kuni Takaniro")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
