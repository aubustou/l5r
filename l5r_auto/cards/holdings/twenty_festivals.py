from __future__ import annotations

from l5r_auto.keywords import (
    Barracks,
    Destined,
    Dojo,
    Expendable,
    Fortification,
    Kharmic,
    Legacy,
    Library,
    Market,
    Port,
    Temple,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

Blessed_Herbalist = Holding(
    card_id=12068,
    title="Blessed Herbalist",
    gold_cost=2,
    gold_production="2",
    keywords=[Expendable, Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Distracted_Sentries = Holding(
    card_id=12069,
    title="Distracted Sentries",
    gold_cost=6,
    gold_production="5",
    keywords=[Fortification, Kharmic],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Elemental_Library = Holding(
    card_id=12070,
    title="Elemental Library",
    gold_cost=2,
    gold_production="2",
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Forgotten_Legacy = Holding(
    card_id=12071,
    title="Forgotten Legacy",
    gold_cost=3,
    gold_production="3",
    keywords=[Legacy],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Forward_Encampment = Holding(
    card_id=12072,
    title="Forward Encampment",
    gold_cost=2,
    gold_production="2",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
KaiuBuilt_Defenses = Holding(
    card_id=12073,
    title="Kaiu-Built Defenses",
    gold_cost=0,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Labor_Crew = Holding(
    card_id=12074,
    title="Labor Crew",
    gold_cost=2,
    gold_production="2",
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Personal_Dojo = Holding(
    card_id=12075,
    title="Personal Dojo",
    gold_cost=3,
    gold_production="3",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Questionable_Market = Holding(
    card_id=12076,
    title="Questionable Market",
    gold_cost=1,
    gold_production="1",
    keywords=[Market, Port],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Secret_Dojo = Holding(
    card_id=12077,
    title="Secret Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Temple_of_Destiny = Holding(
    card_id=12078,
    title="Temple of Destiny",
    gold_cost=1,
    gold_production="1",
    keywords=[Destined, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
The_Obsidian_Dojo = Holding(
    card_id=12079,
    title="The Obsidian Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Throes_of_Madness = Holding(
    card_id=12080,
    title="Throes of Madness",
    gold_cost=2,
    gold_production="2",
    keywords=[Kharmic],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
