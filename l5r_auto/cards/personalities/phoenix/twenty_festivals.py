from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Alchemist,
    Artisan,
    Cavalry,
    Commander,
    Daimyo,
    Duelist,
    Earth,
    Experienced,
    Fire,
    Inquisitor,
    Loyal,
    Magistrate,
    Naval,
    Samurai,
    Shugenja,
    SoulOf,
    Unique,
    Water,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i>"
Agasha_Shikeno = Personality(
    card_id=12140,
    title="Agasha Shikeno",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Air, Alchemist, Fire, Shugenja, SoulOf("Asako Hoshimi")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Water Interrupt:</b> After the action Equips a Spell to Tameko, take an additional action."
Agasha_Tameko = Personality(
    card_id=12141,
    title="Agasha Tameko",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Commander, Shugenja, SoulOf("Agasha Tomioko"), Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Open:</b> Target a Personality. You suspect him of the taint. If he has <b>Shadowlands, </b>give him -2F. He has <b>Shadowlands </b>while you are taking actions <i>(this turn)</i>."
Asako_Hiribe = Personality(
    card_id=12142,
    title="Asako Hiribe",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Earth, Inquisitor, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Battle:</b> Bow a target enemy Personality. If he is Shadowlands, give each Shugenja in this army +1F."
Asako_Tsunefusa_Experienced = Personality(
    card_id=12143,
    title="Asako Tsunefusa",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=9,
    honor_requirement=8,
    clan=[PhoenixClan],
    keywords=[
        Loyal,
        Unique,
        Daimyo,
        Earth,
        Experienced("1"),
        Inquisitor,
        Magistrate,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Air Open, :bow::</b> Target a Phoenix Clan Personality in your discard pile. The rebirth begins. He becomes honorably dead."
Isawa_Akime = Personality(
    card_id=12144,
    title="Isawa Akime",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=8,
    clan=[PhoenixClan],
    keywords=[Air, Artisan, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Battle, :bow::</b> You may bow one of Haruge's Spells to straighten her. Bow a target enemy Personality. If it is an Oni, it will not straighten until the next turn ends."
Isawa_Haruge = Personality(
    card_id=12145,
    title="Isawa Haruge",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Earth, Shugenja, SoulOf("Isawa Itsuoko")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Loyal Personalities will not join other Clans. Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit. Shugenja may attach and cast Spells.)</i>"
Isawa_Kageharu = Personality(
    card_id=12146,
    title="Isawa Kageharu",
    force=1,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Loyal, Naval, Shugenja, SoulOf("Isawa Mizuhiko"), Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i><br><b>Water Battle:</b> If he would be opposed, move your target Personality at any location to a battlefield <i>(not necessarily this one)</i>."
Isawa_Mochiko = Personality(
    card_id=12147,
    title="Isawa Mochiko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=2,
    clan=[PhoenixClan],
    keywords=[Cavalry, Shugenja, SoulOf("Isawa Tanaka"), Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Water Battle:</b> If he would be opposed, move to this battlefield a target Personality at any location. Straighten his unit as he moves."
Isawa_Uzuyumi_Experienced = Personality(
    card_id=12148,
    title="Isawa Uzuyumi",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Naval, Unique, Commander, Experienced("1"), Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged Attack equal to Danjiro's Force."
Shiba_Danjiro = Personality(
    card_id=12149,
    title="Shiba Danjiro",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=0,
    clan=[PhoenixClan],
    keywords=[Samurai, SoulOf("Shiba Morihiko"), Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>After the first time each turn Kiyomichi assigns to an army with a Shugenja, gain 1 Honor.<br><b>Battle:</b> Move your target Shugenja at any location to Kiyomichi's battlefield."
Shiba_Kiyomichi = Personality(
    card_id=12150,
    title="Shiba Kiyomichi",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=12,
    clan=[PhoenixClan],
    keywords=[Duelist, Samurai, SoulOf("Shiba Sakishi"), Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
