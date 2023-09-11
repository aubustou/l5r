from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Commander,
    Duelist,
    Experienced,
    Magistrate,
    Reserve,
    Resilient,
    Samurai,
    ScionOfStone,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Increase Kano's Force bonuses from the rulebook Tactical Advantage action by 2 if he has a Tessen.<br><b>Battle:</b> Give a target Battle Strategy without Discipline in your discard pile Discipline :g2:."
Akodo_Kano_Master_Tactician_Experienced_2 = Personality(
    card_id=12302,
    title="Akodo Kano, Master Tactician",
    force=3,
    chi=4,
    personal_honor=4,
    gold_cost=9,
    honor_requirement=12,
    clan=[LionClan],
    keywords=[Experienced("2"), Tactician, Unique, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Iaijutsu Battle:</b> Naotaka challenges a target enemy Personality. Give the winner +2F."
Akodo_Naotaka = Personality(
    card_id=12303,
    title="Akodo Naotaka",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Toshigure has -1C while dueling Doji Moro. Toshigure has +1PH if he won a duel this turn or you are Mantis Clan."
Akodo_Toshigure = Personality(
    card_id=12304,
    title="Akodo Toshigure",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Battle:</b> Give a target enemy Personality -2F. If he is Scorpion Clan, give Kiyomako +1F."
Ikoma_Kiyomako = Personality(
    card_id=12305,
    title="Ikoma Kiyomako",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: Equipping Nonhuman Followers to Hideyuki is a Battle/Open for you, for 1 less gold if Hideyuki entered play this battle. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Matsu_Hideyuki = Personality(
    card_id=12306,
    title="Matsu Hideyuki",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Reserve, Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"You may destroy one of Kaori's unbowed Nonhuman Followers to refuse a challenge targeting her and negate all effects of refusing.<br><b>Earth Battle:</b> Fear 2."
Matsu_Kaori = Personality(
    card_id=12307,
    title="Matsu Kaori",
    force=4,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=5,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai, ScionOfStone],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
