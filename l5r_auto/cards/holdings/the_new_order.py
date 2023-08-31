from __future__ import annotations

from l5r_auto.keywords import (
    Expendable,
    Fortification,
    GeishaHouse,
    Imperial,
    Jade,
    Kharmic,
    Library,
    Market,
    Mine,
    Retainer,
    Shadowlands,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

Contemplative_Shrine = Holding(
    card_id=11883,
    title="Contemplative Shrine",
    gold_cost=3,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Delicate_Forge = Holding(
    card_id=11878,
    title="Delicate Forge",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Developed_Quarry = Holding(
    card_id=11869,
    title="Developed Quarry",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Earthborn_Temple = Holding(
    card_id=11870,
    title="Earthborn Temple",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
House_of_No_Tomorrow = Holding(
    card_id=11873,
    title="House of No Tomorrow",
    gold_cost=2,
    keywords=[Fortification, GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Jade_Bazaar = Holding(
    card_id=11874,
    title="Jade Bazaar",
    gold_cost=5,
    keywords=[Jade, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Lane_of_Immorality = Holding(
    card_id=11880,
    title="Lane of Immorality",
    gold_cost=1,
    keywords=[Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Missing_Caravan = Holding(
    card_id=11877,
    title="Missing Caravan",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Otomo_Bureaucrat = Holding(
    card_id=11879,
    title="Otomo Bureaucrat",
    gold_cost=6,
    keywords=[Imperial, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Plain_Library = Holding(
    card_id=11875,
    title="Plain Library",
    gold_cost=3,
    keywords=[Expendable, Fortification, Library],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Protected_Temple = Holding(
    card_id=11871,
    title="Protected Temple",
    gold_cost=5,
    keywords=[Fortification, Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Remote_Temple = Holding(
    card_id=11881,
    title="Remote Temple",
    gold_cost=1,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Rich_Vein = Holding(
    card_id=11872,
    title="Rich Vein",
    gold_cost=3,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shrine_of_the_Colonies = Holding(
    card_id=11882,
    title="Shrine of the Colonies",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
The_Toil_of_Zokujin = Holding(
    card_id=11868,
    title="The Toil of Zokujin",
    gold_cost=1,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Weapon_Artist = Holding(
    card_id=11876,
    title="Weapon Artist",
    gold_cost=7,
    keywords=[Mine, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
