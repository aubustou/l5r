from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Cavalry,
    Courtier,
    DeathPriest,
    Expendable,
    Merchant,
    Samurai,
    Shugenja,
    StableMaster,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Ide_Aragaki = Personality(
    id=11781,
    title="Ide Aragaki",
    force=1,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Ide_Kosaka = Personality(
    id=11782,
    title="Ide Kosaka",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Moto_Erdene = Personality(
    id=11783,
    title="Moto Erdene",
    force=2,
    chi=1,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Expendable, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Moto_Qorin = Personality(
    id=11784,
    title="Moto Qorin",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Shinjo_Ajasu_Topaz_Champion = Personality(
    id=11785,
    title="Shinjo Ajasu, Topaz Champion",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=5,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
Utaku_Saiken = Personality(
    id=11786,
    title="Utaku Saiken",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Samurai, StableMaster],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, ModernEdition, TwentyFestivalsEdition],
)
