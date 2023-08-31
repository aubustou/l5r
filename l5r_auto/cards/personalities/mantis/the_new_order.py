from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Earth,
    Expendable,
    Kolat,
    Magistrate,
    Naval,
    Pirate,
    Samurai,
    Scout,
    Shugenja,
    TheMaskedWasp,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Kitsune_Gorikki = Personality(
    card_id=11909,
    title="Kitsune Gorikki",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Expendable, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kitsune_Yoshioka = Personality(
    card_id=11908,
    title="Kitsune Yoshioka",
    force=0,
    chi=2,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tsuruchi_Satou = Personality(
    card_id=11911,
    title="Tsuruchi Satou",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Samurai, Scout, TheMaskedWasp],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Nishigori = Personality(
    card_id=11910,
    title="Yoritomo Nishigori",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Raiden = Personality(
    card_id=11912,
    title="Yoritomo Raiden",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Kolat, Pirate],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Yoritomo_Yakuwa = Personality(
    card_id=11913,
    title="Yoritomo Yakuwa",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
