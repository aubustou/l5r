from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Commander,
    Destined,
    Experienced,
    Magistrate,
    Reserve,
    Samurai,
    Scout,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Moto_Baatar = Personality(
    id=12337,
    title="Moto Baatar",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shinjo_Chairei = Personality(
    id=12338,
    title="Shinjo Chairei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shinjo_Tsungmin = Personality(
    id=12339,
    title="Shinjo Tsung-min",
    force=3,
    chi=1,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Utaku_Masako = Personality(
    id=12340,
    title="Utaku Masako",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Utaku_Sakiko_Experienced = Personality(
    id=12341,
    title="Utaku Sakiko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=5,
    clan=[UnicornClan],
    keywords=[
        Cavalry,
        Destined,
        Reserve,
        BattleMaiden,
        Experienced("1"),
        Magistrate,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Utaku_Zo_Sia = Personality(
    id=12342,
    title="Utaku Zo Sia",
    force=1,
    chi=2,
    personal_honor=4,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
