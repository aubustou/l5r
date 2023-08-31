from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Commander,
    Duelist,
    Experienced,
    Magistrate,
    Reserve,
    Resilient,
    Samurai,
    ScionOfStone,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

Akodo_Kano_Master_Tactician_Experienced_2 = Personality(
    id=12302,
    title="Akodo Kano, Master Tactician",
    force=3,
    chi=4,
    personal_honor=4,
    gold_cost=9,
    honor_requirement=12,
    clan=[LionClan],
    keywords=[Experienced("2"), Tactician, Unique, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Akodo_Naotaka = Personality(
    id=12303,
    title="Akodo Naotaka",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Akodo_Toshigure = Personality(
    id=12304,
    title="Akodo Toshigure",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Ikoma_Kiyomako = Personality(
    id=12305,
    title="Ikoma Kiyomako",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Hideyuki = Personality(
    id=12306,
    title="Matsu Hideyuki",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Reserve, Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Matsu_Kaori = Personality(
    id=12307,
    title="Matsu Kaori",
    force=4,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=5,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai, ScionOfStone],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
