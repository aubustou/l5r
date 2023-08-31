from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    BitterLies,
    Courtier,
    Expendable,
    Junshin,
    Kensai,
    Mastermind,
    Ninja,
    SakeAddict,
    Samurai,
    Spy,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Bayushi_Akagi = Personality(
    id=11764,
    title="Bayushi Akagi",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Bayushi_Fuyuko = Personality(
    id=11765,
    title="Bayushi Fuyuko",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Bayushi_JinnJa = Personality(
    id=11766,
    title="Bayushi Jinn-Ja",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Mastermind, SakeAddict],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Bayushi_Kotomuri = Personality(
    id=11767,
    title="Bayushi Kotomuri",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Expendable, Junshin, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shosuro_Kayo = Personality(
    id=11768,
    title="Shosuro Kayo",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shosuro_Sadao = Personality(
    id=11769,
    title="Shosuro Sadao",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Ninja, Samurai, Spy],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
