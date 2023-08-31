from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Earth,
    Experienced,
    Jade,
    Kolat,
    LadyOfTheSun,
    Magistrate,
    Naval,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    Thunder,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Kitsune_Beiko = Personality(
    id=11752,
    title="Kitsune Beiko",
    force=0,
    chi=1,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Moshi_Raiko = Personality(
    id=11753,
    title="Moshi Raiko",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, LadyOfTheSun, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tsuruchi_Hikari = Personality(
    id=11754,
    title="Tsuruchi Hikari",
    force=2,
    chi=1,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tsuruchi_Yashiro_Defender_of_the_Obsidian_Blades_Experienced = Personality(
    id=11755,
    title="Tsuruchi Yashiro, Defender of the Obsidian Blades",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Unique, Experienced("1"), Jade, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Shotsuo = Personality(
    id=11756,
    title="Yoritomo Shotsuo",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Yusuke = Personality(
    id=11757,
    title="Yoritomo Yusuke",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kolat, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
