from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import (
    Ashigaru,
    Conqueror,
    Experienced,
    Kensai,
    Monk,
    Naval,
    Nonhuman,
    Oni,
    Resilient,
    Shadowlands,
    Shugenja,
    Unique,
    Water,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"After Akuma enters play, lose 4 Honor. Will not attach cards.<br><b>Battle:</b> Destroy a target enemy attachment with equal or lower Force."
Akuma_no_Obake = Personality(
    card_id=12488,
    title="Akuma no Obake",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Keisho will not attach Spells with Focus Value greater than her Chi."
Keisho = Personality(
    card_id=12489,
    title="Keisho",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Resilient, Ashigaru, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Will not join a Spider Clan player.<br><b>Battle, :bow::</b> Melee 4 Attack. You may bow Tetsuo's Polearm to straighten him."
Tetsuo_Experienced_2 = Personality(
    card_id=12490,
    title="Tetsuo",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=10,
    honor_requirement=None,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Conqueror, Experienced("2"), Kensai, Unique, Monk],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After The Crimson Mountain Oni enters play, lose 7 Honor. Will not attach cards or issue challenges.<br><b>Interrupt:</b> Negate The Crimson Mountain Oni's movement from the action.<br><b>Battle:</b> Melee 6 Attack. If this destroys an attachment on a Crab Clan Personality, you may make a Melee 6 Attack."
The_Crimson_Mountain_Oni = Personality(
    card_id=12491,
    title="The Crimson Mountain Oni",
    force=7,
    chi=6,
    personal_honor=0,
    gold_cost=14,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Resilient, Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br>After Umikaiju enters play, lose 2 Honor. Will not attach cards.<br><b>Battle, :bow::</b> Fear 5."
Umikaiju = Personality(
    card_id=12492,
    title="Umikaiju",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Naval, Nonhuman, Oni, Shadowlands, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
