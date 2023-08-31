from __future__ import annotations

from l5r_auto.keywords import (
    Barrack,
    Barracks,
    Dojo,
    Farm,
    Fortification,
    Retainer,
    Winter,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

Architect = Holding(
    card_id=12268,
    title="Architect",
    gold_cost=3,
    gold_production="3",
    keywords=[Fortification, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Ashigaru_Farmland = Holding(
    card_id=12269,
    title="Ashigaru Farmland",
    gold_cost=3,
    gold_production="3",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Bamboo_Irrigation = Holding(
    card_id=12270,
    title="Bamboo Irrigation",
    gold_cost=1,
    gold_production="1*",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Borderless_Fields = Holding(
    card_id=12271,
    title="Borderless Fields",
    gold_cost=2,
    gold_production="2",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Combat_Drill_Field = Holding(
    card_id=12272,
    title="Combat Drill Field",
    gold_cost=1,
    gold_production="1",
    keywords=[Barrack],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Daikura = Holding(
    card_id=12273,
    title="Daikura",
    gold_cost=3,
    gold_production="3",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Garrison_Hub = Holding(
    card_id=12274,
    title="Garrison Hub",
    gold_cost=2,
    gold_production="2",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Hasty_Defenses = Holding(
    card_id=12275,
    title="Hasty Defenses",
    gold_cost=2,
    gold_production="2",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Heisha = Holding(
    card_id=12276,
    title="Heisha",
    gold_cost=6,
    gold_production="5",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Isolated_Farmlands = Holding(
    card_id=12277,
    title="Isolated Farmlands",
    gold_cost=6,
    gold_production="5",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Mess_Hall = Holding(
    card_id=12278,
    title="Mess Hall",
    gold_cost=3,
    gold_production="2*",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Officers_Lodge = Holding(
    card_id=12279,
    title="Officer's Lodge",
    gold_cost=3,
    gold_production="3",
    keywords=[Barracks, Winter],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Padis_Dojo = Holding(
    card_id=12280,
    title="Padis Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Peaceful_Retreat = Holding(
    card_id=12281,
    title="Peaceful Retreat",
    gold_cost=4,
    gold_production="4",
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Rhetorician = Holding(
    card_id=12282,
    title="Rhetorician",
    gold_cost=3,
    gold_production="3",
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Veterans_Farmland = Holding(
    card_id=12283,
    title="Veteran's Farmland",
    gold_cost=2,
    gold_production="2",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
