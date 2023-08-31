from __future__ import annotations

from l5r_auto.keywords import (
    Dojo,
    Fortification,
    GeishaHouse,
    Imperial,
    Kharmic,
    Market,
    Port,
    SakeHouse,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

Coastal_Lane = Holding(
    card_id=11547,
    title="Coastal Lane",
    gold_cost=4,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Colonial_Market = Holding(
    card_id=11548,
    title="Colonial Market",
    gold_cost=5,
    keywords=[Kharmic, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Contested_Market = Holding(
    card_id=11549,
    title="Contested Market",
    gold_cost=2,
    keywords=[Market, Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hanamachi = Holding(
    card_id=11550,
    title="Hanamachi",
    gold_cost=4,
    keywords=[Kharmic, GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
House_of_Floating_Petals = Holding(
    card_id=11551,
    title="House of Floating Petals",
    gold_cost=3,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
House_of_Loose_Silk = Holding(
    card_id=11552,
    title="House of Loose Silk",
    gold_cost=6,
    keywords=[GeishaHouse, SakeHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
House_of_the_Floating_Lotus = Holding(
    card_id=11553,
    title="House of the Floating Lotus",
    gold_cost=3,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kumite_Grounds = Holding(
    card_id=11554,
    title="Kumite Grounds",
    gold_cost=2,
    keywords=[Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Lonely_Dojo = Holding(
    card_id=11555,
    title="Lonely Dojo",
    gold_cost=2,
    keywords=[Kharmic, Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Momijis_Chambers = Holding(
    card_id=11556,
    title="Momiji's Chambers",
    gold_cost=1,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
MushaGaeshi = Holding(
    card_id=11557,
    title="Musha-Gaeshi",
    gold_cost=3,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Second_City_Harbor = Holding(
    card_id=11558,
    title="Second City Harbor",
    gold_cost=2,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Second_City_Market = Holding(
    card_id=11559,
    title="Second City Market",
    gold_cost=1,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
The_Inner_Ring = Holding(
    card_id=11560,
    title="The Inner Ring",
    gold_cost=2,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
The_Ivory_Courtroom = Holding(
    card_id=11561,
    title="The Ivory Courtroom",
    gold_cost=2,
    keywords=[Imperial],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
