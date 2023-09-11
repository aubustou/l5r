from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Alchemist,
    Cavalry,
    Earth,
    Experienced,
    Inquisitor,
    Jade,
    Loyal,
    Magistrate,
    Resilient,
    Samurai,
    Shugenja,
    TheMaskedPhoenix,
    Unique,
    Void,
    Water,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"After you Recruit Dorai from a Province, refill it face-up.<br><b>Void Open:</b> Give Kharmic to a face-up Library or Temple in your Province."
Agasha_Dorai = Personality(
    card_id=12470,
    title="Agasha Dorai",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[PhoenixClan],
    keywords=[Air, Alchemist, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Your Earth and Jade Spells out of play have <b>Honor </b>and<b> Kharmic </b>while another player controls any Shadowlands Personalities. After an action from an Earth or Jade card in this unit bows or destroys an enemy Shadowlands card, gain 1 Honor."
Asako_Misai = Personality(
    card_id=12471,
    title="Asako Misai",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Earth, Inquisitor, Magistrate, Shugenja, TheMaskedPhoenix],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Enters play for 2 less Gold if you are Crab Clan or have <b>Compassion </b>or<b> Courtesy</b>. <i>(Compassion takes effect while you have fewer Provinces than anyone else. Courtesy does not take effect if you went first.)</i>"
Isawa_Bikaru = Personality(
    card_id=12472,
    title="Isawa Bikaru",
    force=4,
    chi=4,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=3,
    clan=[PhoenixClan],
    keywords=[Resilient, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear equal to Hokaiko's Force that may target Items and Spells. If Hokaiko has moved this turn, this Fear destroys attachments after it bows them."
Isawa_Hokaiko = Personality(
    card_id=12473,
    title="Isawa Hokaiko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Your other Earth Shugenja have +1F.<br><b>Earth Jade Battle:</b> Melee 3 Attack, or Melee 5 Attack if the target is Shadowlands."
Isawa_Norimichi_Elemental_Master_Experienced_2 = Personality(
    card_id=12474,
    title="Isawa Norimichi, Elemental Master",
    force=5,
    chi=5,
    personal_honor=3,
    gold_cost=11,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Experienced("2"), Loyal, Unique, Earth, Jade, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Void Battle:</b> Ranged Attack equal to the number of Kiho and Spell actions you have resolved this battle, or 2, whichever is greater. You may target and move your Shugenja at any location home or, if he or she would be opposed, to this battlefield."
Shiba_Kakei_Experienced = Personality(
    card_id=12475,
    title="Shiba Kakei",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Cavalry, Experienced("1"), Samurai, Void, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
