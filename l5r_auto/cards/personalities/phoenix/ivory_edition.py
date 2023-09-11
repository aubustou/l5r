from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import (
    Air,
    Alchemist,
    Cavalry,
    ClanChampion,
    Daimyo,
    Duelist,
    Earth,
    ElementalMaster,
    Experienced,
    Fire,
    Loyal,
    Monk,
    Mountaineer,
    RitualMaster,
    Samurai,
    ShibasSoul,
    Shugenja,
    SoulOf,
    TheBlindPhoenix,
    TheInfiniteEye,
    Unique,
    Void,
    Water,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Shugenja may attach and cast Spells.)</i><br><b>Fire Void Battle:</b> Discard a card with an element keyword to give Kyokuta a Force bonus equal to the card's Focus Value. You may make a Ranged Attack with strength equal to that Focus Value."
Agasha_Kyokuta = Personality(
    card_id=11198,
    title="Agasha Kyokuta",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Alchemist, Fire, Shugenja, SoulOf("Agasha Yuhiko"), Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Void Battle:</b> Discard a Kiho or a Spell from your hand to bow a target enemy card."
Asako_Sadaki = Personality(
    card_id=11199,
    title="Asako Sadaki",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=0,
    clan=[PhoenixClan, BrotherhoodOfShinsei],
    keywords=[Monk, SoulOf("Asako Suda"), Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Earth Interrupt:</b> If the action is an Attacker's Battle action taken before the Defender's first opportunity to act or pass, discard a card to negate its effects, and gain 2 Honor if the card was a Spell."
Isawa_Amihiko = Personality(
    card_id=11200,
    title="Isawa Amihiko",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Earth, Mountaineer, Shugenja, SoulOf("Isawa Wakasa")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battlefield. Shugenja may attach and cast spells.)</i><br><b>Air Battle, :bow::</b> Move home a target Personality."
Isawa_Kamiko = Personality(
    card_id=11201,
    title="Isawa Kamiko",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=3,
    clan=[PhoenixClan],
    keywords=[Cavalry, Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Earth Battle, :gstar::</b> Equip a Spell to Kosea. You may take an additional action from the Spell."
Isawa_Kosea = Personality(
    card_id=11202,
    title="Isawa Kosea",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Void Tireless Open:</b> Give Kouka <b>Air, Earth, Fire,</b> or <b>Water</b>. <i>(Tireless actions can be taken even while bowed.)</i>"
Isawa_Kouka = Personality(
    card_id=11203,
    title="Isawa Kouka",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Shugenja, SoulOf("Isawa Kimi"), Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Before you draw cards at the end of your turn, draw a card.<br><b>Void Home Battle, :bow::</b> Give all your opposed Samurai +1F, or all enemy Personalities -1F."
Isawa_Shunryu_the_Infinite_Eye = Personality(
    card_id=11204,
    title="Isawa Shunryu, the Infinite Eye",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=10,
    clan=[PhoenixClan],
    keywords=[Loyal, Unique, ElementalMaster, Shugenja, TheInfiniteEye, Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i> <br><b>Water Home Battle, :bow::</b> Move a target unit at any battlefield to a different, unresolved battlefield."
Isawa_Uzuyumi = Personality(
    card_id=11205,
    title="Isawa Uzuyumi",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=5,
    clan=[PhoenixClan],
    keywords=[Shugenja, SoulOf("Isawa Riake"), Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"Before your Spell or Kiho action resolves, if Eraki is at the current battlefield, give him +1F/+1C."
Shiba_Eraki = Personality(
    card_id=11206,
    title="Shiba Eraki",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[PhoenixClan],
    keywords=[RitualMaster, Samurai, SoulOf("Shiba Yoma"), Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After you lose Honor from your own cards, Michiki commits Seppuku. <i><i>(Honor loss from dying dishonorably is from the rulebook, not your own cards.)</i></i>"
Shiba_Michiki = Personality(
    card_id=11207,
    title="Shiba Michiki",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After a Spell action that targeted Myoushi resolves, give him a <b>Void</b> token. <br><b>Repeatable Battle/Open:</b> Destroy a Void token on Myoushi to give him +1F, +1C, or +1PH."
Shiba_Myoushi = Personality(
    card_id=11208,
    title="Shiba Myoushi",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Samurai, SoulOf("Shiba Yobei"), Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Tsukimi is not Unique)</i>.<br>Tsukimi has the element keywords of all Personalities you control. Tsukimi can attach Spells and has <b>Shugenja</b> while she has a Spell."
Shiba_Tsukimi_the_Blind_Phoenix_Experienced_5 = Personality(
    card_id=11209,
    title="Shiba Tsukimi, the Blind Phoenix",
    force=4,
    chi=5,
    personal_honor=5,
    gold_cost=12,
    honor_requirement=10,
    clan=[PhoenixClan],
    keywords=[
        Cavalry,
        Duelist,
        Experienced("5"),
        Loyal,
        ClanChampion,
        Daimyo,
        Samurai,
        ShibasSoul,
        TheBlindPhoenix,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
