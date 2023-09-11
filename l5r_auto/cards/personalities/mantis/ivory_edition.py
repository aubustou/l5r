from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    BountyHunter,
    ClanChampion,
    Earth,
    Experienced,
    Kensai,
    Loyal,
    Magistrate,
    Naval,
    Samurai,
    Scout,
    Shugenja,
    SoulOf,
    TheGrowingStorm,
    Thunder,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

'<i>(Shugenja may attach and cast Spells.)</i><br><b>Earth Interrupt:</b> After you Recruit Parumba, create a 3F/2C/3PH <b>Mantis Clan &#149; Boar &#149; Nonhuman &#149; Spirit</b> Personality with the ability, "<b>Battle:</b> Melee 2 Attack."'
Kitsune_Parumba = Personality(
    card_id=11188,
    title="Kitsune Parumba",
    force=0,
    chi=2,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit. Shugenja may attach and cast Spells.)</i><br><b>Thunder Battle:</b> Fear 2."
Moshi_Madohime = Personality(
    card_id=11189,
    title="Moshi Madohime",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, Scout, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack.<br><b>Tireless Battle:</b> Move Kaito home."
Tsuruchi_Kaito = Personality(
    card_id=11190,
    title="Tsuruchi Kaito",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> Give one of the action's Ranged Attacks +1 strength."
Tsuruchi_Natsuki = Personality(
    card_id=11191,
    title="Tsuruchi Natsuki",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Magistrate, Samurai, SoulOf("Tsuruchi Masako")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 2 Attack. If this destroys a card, produce 1 Gold <i>(which can be used later this phase)</i>."
Tsuruchi_Rin = Personality(
    card_id=11192,
    title="Tsuruchi Rin",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[BountyHunter, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Personalities opposing Hiromi have -1F if you took the first Battle action in this battle <i>(including during that action)</i>.<br><b>Thunder Engage:</b> Your Ranged Attacks during this battle have +1 strength."
Yoritomo_Hiromi_the_Growing_Storm_Experienced_2 = Personality(
    card_id=11193,
    title="Yoritomo Hiromi, the Growing Storm",
    force=4,
    chi=5,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=4,
    clan=[MantisClan],
    keywords=[
        Experienced("2"),
        Kensai,
        Loyal,
        Naval,
        Unique,
        ClanChampion,
        Samurai,
        TheGrowingStorm,
        Thunder,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br><b>Battle, :bow::</b> Move a target enemy non-Naval Personality home and bow his unit as he moves."
Yoritomo_Ichido = Personality(
    card_id=11194,
    title="Yoritomo Ichido",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, Samurai, SoulOf("Kindari")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br>Equipping Weapons to Matsuo is a <b>Battle/Open</b> action for you."
Yoritomo_Matsuo = Personality(
    card_id=11195,
    title="Yoritomo Matsuo",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Naval, Samurai, SoulOf("Seppun Matsuo")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i> <br><b>Battle:</b> Personalities that did not assign to this battlefield cannot move here."
Yoritomo_Takuya = Personality(
    card_id=11196,
    title="Yoritomo Takuya",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai, SoulOf("Yoritomo Bussho")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i></i>"
Yoritomo_Teihiko = Personality(
    card_id=11197,
    title="Yoritomo Teihiko",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai, SoulOf("Yoritomo Mie")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
