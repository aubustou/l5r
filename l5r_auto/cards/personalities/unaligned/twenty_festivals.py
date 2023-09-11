from __future__ import annotations

from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Courtier,
    Dragon,
    DragonflyClan,
    Earth,
    Experienced,
    Fire,
    Magistrate,
    Naval,
    Nonhuman,
    Samurai,
    Shadowlands,
    Shugenja,
    SoulOf,
    Undead,
    Unique,
    Void,
    Water,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot attach Followers or Items. Cannot gain a Clan Alignment. Has -2HR while you control the Ring of Air. After a phase begins, straighten Air Dragon.<br><b>Air Battle:</b> Negate Air Dragon's current Force penalties."
Air_Dragon_Experienced_3 = Personality(
    card_id=12171,
    title="Air Dragon",
    force=7,
    chi=5,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=15,
    clan=[Unaligned],
    keywords=[Cavalry, Experienced("3"), Unique, Air, Dragon, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cannot attach Followers or Items. Cannot gain a Clan Alignment. Has -2HR while you control the Ring of Earth. Before the first time each turn another player's action moves or bows the Earth Dragon, negate it."
Earth_Dragon_Experienced_2 = Personality(
    card_id=12172,
    title="Earth Dragon",
    force=7,
    chi=5,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=15,
    clan=[Unaligned],
    keywords=[Cavalry, Experienced("2"), Unique, Dragon, Earth, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cannot attach Followers or Items. Cannot gain a Clan Alignment except Phoenix Clan. Has -2HR while you control the Ring of Fire.<br><b>Fire Battle, :bow::</b> Ranged 7 Attack."
Fire_Dragon_Experienced_3 = Personality(
    card_id=12173,
    title="Fire Dragon",
    force=7,
    chi=5,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=15,
    clan=[Unaligned],
    keywords=[Cavalry, Experienced("3"), Unique, Dragon, Fire, Nonhuman, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :bow::</b> Target a dishonorable Personality. After the next time this turn he attacks you or an action on his card resolves, gain 1 Honor."
Haikitsu = Personality(
    card_id=12174,
    title="Haikitsu",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[Unaligned],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :g3::</b> Put a Ring from your hand into play; while it remains in play, it does not count towards an Enlightenment Victory. After your next turn begins, put it into your hand."
Kungan = Personality(
    card_id=12175,
    title="Kung-an",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br>After Daigoro enters play, lose 4 Honor.<br><b>Battle:</b> Fear 4."
Moto_Daigoro = Personality(
    card_id=12176,
    title="Moto Daigoro",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Cavalry, Nonhuman, Samurai, Shadowlands, Undead],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Terumoto enters play, gain 1 Honor."
Otomo_Terumoto = Personality(
    card_id=12177,
    title="Otomo Terumoto",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Courtier, Samurai, SoulOf("Otomo Taneji")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'<i>(This Personality is Unaligned.)</i> <br><b>Invest :g5::</b> Give Jairyu a +1F/+1C token and the permanent ability, "<b>Water Battle:</b> Move home a target defending Personality."'
Tonbo_Jairyu = Personality(
    card_id=12178,
    title="Tonbo Jairyu",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[Unaligned],
    keywords=[Naval, DragonflyClan, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cannot attach Followers or Items. Cannot gain a Clan Alignment. Has -2HR while you control the Ring of the Void. After the Void Dragon's army destroys any units or Province in a battle resolution, the enemy leader discards two cards from his hand."
Void_Dragon_Experienced_3 = Personality(
    card_id=12179,
    title="Void Dragon",
    force=7,
    chi=5,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=15,
    clan=[Unaligned],
    keywords=[Cavalry, Experienced("3"), Unique, Dragon, Nonhuman, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cannot attach Followers or Items. Cannot gain a Clan Alignment. Has -2HR while you control the Ring of Water.<br><b>Water Tireless Open:</b> Water Dragon copies another target Personality's keyword, trait, or ability that does not copy abilities."
Water_Dragon_Experienced_3 = Personality(
    card_id=12180,
    title="Water Dragon",
    force=7,
    chi=5,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=15,
    clan=[Unaligned],
    keywords=[Cavalry, Experienced("3"), Unique, Dragon, Nonhuman, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
