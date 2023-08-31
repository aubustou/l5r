from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Conqueror,
    Experienced,
    Fire,
    Magistrate,
    Samurai,
    Shugenja,
    Unique,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Isawa_Genma = Personality(
    id=11758,
    title="Isawa Genma",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[Cavalry, Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Isawa_Kaname_Advisor_to_the_Ruby_Champion_Experienced = Personality(
    id=11759,
    title="Isawa Kaname, Advisor to the Ruby Champion",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=9,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Unique, Experienced("1"), Fire, Magistrate, Shugenja, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Isawa_Kido = Personality(
    id=11760,
    title="Isawa Kido",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=8,
    clan=[PhoenixClan],
    keywords=[Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Isawa_Muira = Personality(
    id=11761,
    title="Isawa Muira",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[Conqueror, Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shiba_Kakei = Personality(
    id=11762,
    title="Shiba Kakei",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Cavalry, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shiba_Yuuchi = Personality(
    id=11763,
    title="Shiba Yuuchi",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
