from __future__ import annotations

from l5r_auto.clans import NagaFaction, UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    ClanChampion,
    Commander,
    Conqueror,
    Courtier,
    Experienced,
    Guard,
    Imperial,
    Kami,
    Loyal,
    Merchant,
    Naga,
    Paragon,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    SoulOf,
    Tactician,
    TheLivingGoddess,
    Unique,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i><br><b>Political Interrupt, :bow::</b> If the action is Lobby, it does not give the Imperial Favor, and its player may Lobby once more this turn."
Ide_Kotono = Personality(
    card_id=11233,
    title="Ide Kotono",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Courtier, Guard, Imperial, Samurai, SoulOf("Shinjo Haruko")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Economic Open, :bow::</b> If it is another player's turn, he may pay 2 Gold. If he did not, gain 2 Honor."
Ide_Okinomi = Personality(
    card_id=11234,
    title="Ide Okinomi",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Loyal, Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Absent Home Battle, :bow::</b> If he would be opposed, move your target Personality at home to the current battlefield. If he is defending, straighten him as he moves."
Iuchi_Chiwa = Personality(
    card_id=11235,
    title="Iuchi Chiwa",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Shugenja, SoulOf("Iuchi Eiji")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battlefield. Shugenja may attach and cast spells.)</i></i>"
Iuchi_Honma = Personality(
    card_id=11236,
    title="Iuchi Honma",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Cavalry, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battlefield. A Conqueror's unit doesn't bow after battle.)</i></i>"
Moto_Alagh = Personality(
    card_id=11237,
    title="Moto Alagh",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Conqueror, Samurai, SoulOf("Moto Yuudai")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i><br><b>Battle:</b> Bow a target non-Unique enemy Personality with no attachments and higher Force."
Moto_Chinua = Personality(
    card_id=11238,
    title="Moto Chinua",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai, SoulOf("Shinjo Genya")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Infantry Personalities opposing Naleesh have -1F. After you Recruit a Personality during battle, gain 1 Honor.<br><b>Engage:</b> Give <b>Reserve</b> to a target face-up Unicorn Clan Personality in your Province."
Moto_Naleesh_the_Living_Goddess_Experienced = Personality(
    card_id=11239,
    title="Moto Naleesh, the Living Goddess",
    force=4,
    chi=5,
    personal_honor=4,
    gold_cost=10,
    honor_requirement=8,
    clan=[UnicornClan, NagaFaction],
    keywords=[
        Cavalry,
        Loyal,
        Tactician,
        Unique,
        ClanChampion,
        Commander,
        Experienced("1"),
        Kami,
        Naga,
        Paragon,
        Samurai,
        TheLivingGoddess,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Give a target enemy Personality or Follower -3F."
Moto_Okano = Personality(
    card_id=11240,
    title="Moto Okano",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Water Limited:</b> A target Personality in a discard pile becomes honorably dead."
Moto_Ulagan = Personality(
    card_id=11241,
    title="Moto Ulagan",
    force=2,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i></i>"
Shinjo_Okiau = Personality(
    card_id=11242,
    title="Shinjo Okiau",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=2,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai, Scout, SoulOf("Shinjo Aniji")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Fear 3 <i>(Bow a target enemy Follower, or Personality without Followers, with 3 or lower Force)</i>."
Shinjo_Tobita = Personality(
    card_id=11243,
    title="Shinjo Tobita",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(You may Recruit a Reserve Personality, if he would be opposed, as an Absent Battle action.)</i></i>"
Utaku_HyoYeon = Personality(
    card_id=11244,
    title="Utaku Hyo-Yeon",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Cavalry, Loyal, Reserve, Samurai, Scout, SoulOf("Shinjo Hee-Young")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i> <br><b>Battle:</b> Bow a target enemy Infantry Personality with no Followers and lower Force."
Utaku_Izimi = Personality(
    card_id=11245,
    title="Utaku Izimi",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=8,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Samurai, SoulOf("Utaku Etsuko")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
