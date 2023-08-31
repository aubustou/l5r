from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import NagaFaction, UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    ClanChampion,
    Commander,
    Conqueror,
    Courtier,
    Experienced,
    Guard,
    Imperial,
    Kami,
    Loyal,
    Merchant,
    Naga,
    Paragon,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    SoulOf,
    Tactician,
    TheLivingGoddess,
    Unique,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

Ide_Kotono = Personality(
    id=11233,
    title="Ide Kotono",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=6,
    clan=[UnicornClan],
    keywords=[Cavalry, Courtier, Guard, Imperial, Samurai, SoulOf("Shinjo Haruko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Ide_Okinomi = Personality(
    id=11234,
    title="Ide Okinomi",
    force=0,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=6,
    clan=[UnicornClan],
    keywords=[Loyal, Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Iuchi_Chiwa = Personality(
    id=11235,
    title="Iuchi Chiwa",
    force=1,
    chi=3,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Shugenja, SoulOf("Iuchi Eiji")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Iuchi_Honma = Personality(
    id=11236,
    title="Iuchi Honma",
    force=4,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=8,
    clan=[UnicornClan],
    keywords=[Cavalry, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Moto_Alagh = Personality(
    id=11237,
    title="Moto Alagh",
    force=4,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=8,
    clan=[UnicornClan],
    keywords=[Cavalry, Conqueror, Samurai, SoulOf("Moto Yuudai")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Moto_Chinua = Personality(
    id=11238,
    title="Moto Chinua",
    force=2,
    chi=3,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai, SoulOf("Shinjo Genya")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Moto_Naleesh_the_Living_Goddess_Experienced = Personality(
    id=11239,
    title="Moto Naleesh, the Living Goddess",
    force=4,
    chi=5,
    honor_requirement=8,
    personal_honor=4,
    gold_cost=10,
    clan=[UnicornClan, NagaFaction],
    keywords=[
        Cavalry,
        Loyal,
        Tactician,
        Unique,
        ClanChampion,
        Commander,
        Experienced("1"),
        Kami,
        Naga,
        Paragon,
        Samurai,
        TheLivingGoddess,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Moto_Okano = Personality(
    id=11240,
    title="Moto Okano",
    force=3,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Moto_Ulagan = Personality(
    id=11241,
    title="Moto Ulagan",
    force=2,
    chi=4,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Shinjo_Okiau = Personality(
    id=11242,
    title="Shinjo Okiau",
    force=3,
    chi=2,
    honor_requirement=2,
    personal_honor=2,
    gold_cost=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai, Scout, SoulOf("Shinjo Aniji")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Shinjo_Tobita = Personality(
    id=11243,
    title="Shinjo Tobita",
    force=4,
    chi=3,
    honor_requirement=4,
    personal_honor=2,
    gold_cost=7,
    clan=[UnicornClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Utaku_HyoYeon = Personality(
    id=11244,
    title="Utaku Hyo-Yeon",
    force=3,
    chi=2,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=6,
    clan=[UnicornClan],
    keywords=[Cavalry, Loyal, Reserve, Samurai, Scout, SoulOf("Shinjo Hee-Young")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Utaku_Izimi = Personality(
    id=11245,
    title="Utaku Izimi",
    force=4,
    chi=3,
    honor_requirement=8,
    personal_honor=3,
    gold_cost=6,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Samurai, SoulOf("Utaku Etsuko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
