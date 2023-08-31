from __future__ import annotations

from l5r_auto.keywords import (
    Destined,
    Dojo,
    Expendable,
    Experienced,
    Fortification,
    Kharmic,
    Library,
    Nonhuman,
    Oni,
    Retainer,
    Shadowlands,
    Temple,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

City_of_Night_Experienced = Holding(
    card_id=12424,
    title="City of Night",
    gold_cost=1,
    keywords=[Experienced("1"), Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Defensive_Fortification = Holding(
    card_id=12425,
    title="Defensive Fortification",
    gold_cost=3,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Dojo_of_the_Dauntless = Holding(
    card_id=12426,
    title="Dojo of the Dauntless",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Erected_Watchtower = Holding(
    card_id=12427,
    title="Erected Watchtower",
    gold_cost=2,
    keywords=[Expendable, Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
KiRins_Shrine_Experienced_2 = Holding(
    card_id=12428,
    title="Ki-Rin's Shrine",
    gold_cost=1,
    keywords=[Experienced("2"), Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Libraries_of_Kyuden_Isawa = Holding(
    card_id=12429,
    title="Libraries of Kyuden Isawa",
    gold_cost=6,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Master_of_Clear_Water_Dojo = Holding(
    card_id=12430,
    title="Master of Clear Water Dojo",
    gold_cost=3,
    keywords=[Dojo, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Retired_Scholar = Holding(
    card_id=12431,
    title="Retired Scholar",
    gold_cost=2,
    keywords=[Kharmic, Library, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shadowless_Strike_Dojo = Holding(
    card_id=12432,
    title="Shadowless Strike Dojo",
    gold_cost=1,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Shinseis_Last_Hope_Experienced = Holding(
    card_id=12433,
    title="Shinsei's Last Hope",
    gold_cost=4,
    keywords=[Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Spirits_Essence_Dojo = Holding(
    card_id=12434,
    title="Spirit's Essence Dojo",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Temple_of_the_First_Seal = Holding(
    card_id=12435,
    title="Temple of the First Seal",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Feeding_Hills = Holding(
    card_id=12436,
    title="The Feeding Hills",
    gold_cost=3,
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Ikoma_Halls = Holding(
    card_id=12437,
    title="The Ikoma Halls",
    gold_cost=3,
    keywords=[Destined, Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Iron_Mountain_School = Holding(
    card_id=12438,
    title="The Iron Mountain School",
    gold_cost=6,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Miya_Records = Holding(
    card_id=12439,
    title="The Miya Records",
    gold_cost=2,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
