from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Moto_Baatar = Personality(
    id=12337,
    title="Moto Baatar",
    force=3,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=7,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Shinjo_Chairei = Personality(
    id=12338,
    title="Shinjo Chairei",
    force=2,
    chi=3,
    honor_requirement=4,
    personal_honor=3,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Shinjo_Tsungmin = Personality(
    id=12339,
    title="Shinjo Tsung-min",
    force=3,
    chi=1,
    honor_requirement=3,
    personal_honor=2,
    gold_cost=6,
    clan=[UnicornClan],
    keywords=[Cavalry, Reserve, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Utaku_Masako = Personality(
    id=12340,
    title="Utaku Masako",
    force=2,
    chi=2,
    honor_requirement=3,
    personal_honor=3,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Utaku_Sakiko_Experienced = Personality(
    id=12341,
    title="Utaku Sakiko",
    force=3,
    chi=3,
    honor_requirement=5,
    personal_honor=3,
    gold_cost=10,
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
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
Utaku_Zo_Sia = Personality(
    id=12342,
    title="Utaku Zo Sia",
    force=1,
    chi=2,
    honor_requirement=4,
    personal_honor=4,
    gold_cost=5,
    clan=[UnicornClan],
    keywords=[Cavalry],
    traits=[],
    abilities=[],
    legality=[ModernEdition, OnyxEdition, TwentyFestivalsEdition],
)
