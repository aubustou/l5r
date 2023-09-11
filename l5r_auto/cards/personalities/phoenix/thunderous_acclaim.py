from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Earth,
    Expendable,
    Experienced,
    Fire,
    Inquisitor,
    Magistrate,
    Reserve,
    Resilient,
    Samurai,
    Scholar,
    Shugenja,
    Water,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Melee and Ranged Attacks may not target Kazuki. <br><b>Battle, :bow::</b> Fear 4, with +1 strength if the target is Shadowlands, and +1 strength if you have <b>Compassion</b>."
Asako_Kazuki = Personality(
    card_id=12314,
    title="Asako Kazuki",
    force=0,
    chi=1,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Resilient, Earth, Inquisitor, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i>"
Asako_Nashimoto = Personality(
    card_id=12315,
    title="Asako Nashimoto",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=None,
    clan=[PhoenixClan],
    keywords=[Resilient, Earth, Inquisitor, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i> <br><b>Interrupt, :g*::</b> After Fujisawa enters play, Equip a target Spell to him from your hand or discard pile."
Isawa_Fujisawa = Personality(
    card_id=12316,
    title="Isawa Fujisawa",
    force=2,
    chi=5,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Reserve, Scholar, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Ranged Attacks from Hibana's Spells have +1 strength. Hibana has Conqueror while she has a Fire Spell. Hibana Equips Fire Spells for 2 less Gold."
Isawa_Hibana_Experienced = Personality(
    card_id=12317,
    title="Isawa Hibana",
    force=4,
    chi=4,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Experienced("1"), Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br>Compassion, or if any other player is Unicorn Clan: Nobuo has +1F/+1C. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Isawa_Nobuo = Personality(
    card_id=12318,
    title="Isawa Nobuo",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Expendable, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Hano enters the discard pile, he becomes Honorably Dead. Hano Equips Polearms for 1 less Gold.<br><b>Battle:</b> Melee 2 Attack. Gain 1 Honor if this destroyed a card or you are Crane Clan."
Shiba_Hano = Personality(
    card_id=12319,
    title="Shiba Hano",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
