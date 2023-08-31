from __future__ import annotations

from l5r_auto.keywords import (
    Dojo,
    Farm,
    Fortification,
    Imperial,
    Kharmic,
    Market,
    Merchant,
    Retainer,
    SakeHouse,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

Alchemy_Lab = Holding(
    card_id=11712,
    title="Alchemy Lab",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
Bookkeeper = Holding(
    card_id=11713,
    title="Bookkeeper",
    gold_cost=1,
    keywords=[Merchant, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Bountiful_Fields = Holding(
    card_id=11714,
    title="Bountiful Fields",
    gold_cost=4,
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Carpenter_Shrine = Holding(
    card_id=11715,
    title="Carpenter Shrine",
    gold_cost=2,
    keywords=[Fortification, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Cloth_Market = Holding(
    card_id=11716,
    title="Cloth Market",
    gold_cost=5,
    keywords=[Kharmic, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Defensive_Memorial = Holding(
    card_id=11717,
    title="Defensive Memorial",
    gold_cost=2,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Expansive_Range = Holding(
    card_id=11718,
    title="Expansive Range",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Hoteis_Smile = Holding(
    card_id=11719,
    title="Hotei's Smile",
    gold_cost=6,
    keywords=[SakeHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
House_of_Disgrace = Holding(
    card_id=11720,
    title="House of Disgrace",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Kaiu_Engineers = Holding(
    card_id=11721,
    title="Kaiu Engineers",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Shigekawas_Court = Holding(
    card_id=11722,
    title="Shigekawa's Court",
    gold_cost=1,
    keywords=[Imperial, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Summer_Court = Holding(
    card_id=11723,
    title="Summer Court",
    gold_cost=3,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Temple_of_Serenity = Holding(
    card_id=11724,
    title="Temple of Serenity",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Temple_of_the_Heavenly_Crab = Holding(
    card_id=11725,
    title="Temple of the Heavenly Crab",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Tunnel_Network = Holding(
    card_id=11726,
    title="Tunnel Network",
    gold_cost=0,
    keywords=[Fortification, Kharmic],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Voice_of_Experience = Holding(
    card_id=11727,
    title="Voice of Experience",
    gold_cost=3,
    keywords=[Kharmic, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
