from __future__ import annotations

from l5r_auto.clans import (
    BrotherhoodOfShinsei,
    NinjaFaction,
    ShadowlandsFaction,
    SpiderClan,
)
from l5r_auto.keywords import (
    Assassin,
    Conqueror,
    Courtier,
    Kensai,
    Monk,
    Naval,
    Ninja,
    Reserve,
    Resilient,
    Samurai,
    Shadowlands,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action. Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Absent Interrupt:</b> After you Recruit Jemaru, take an additional action.<br><b>Battle:</b> Fear 2."
Daigotsu_Jemaru = Personality(
    card_id=11604,
    title="Daigotsu Jemaru",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Reserve, Resilient, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Invest :g10::</b> Melee 5 Attack <i>(this cannot be Interrupted)</i> that may target a card in a player's home <i>(if otherwise legal)</i>. This Invest cost cannot be reduced. Lose 2 Honor. <br>After Saido enters play, lose 1 Honor."
Goju_Saido = Personality(
    card_id=11605,
    title="Goju Saido",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Assassin, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle. Kensai may attach two Weapons, as long as neither is Two-Handed. Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i>"
Marimako = Personality(
    card_id=11606,
    title="Marimako",
    force=3,
    chi=1,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=0,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Conqueror, Kensai, Naval, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Increase your Honor gain from Proclaiming Jaru to equal the number of Clout tokens, up to 6, in play.<br><b>Political Open, :bow::</b> Discard one or more Clout tokens on other players' cards. Bow a target Personality with Chi equal to the number discarded, and gain that amount of Honor. Give the target a <b>Clout </b>token if he is Crab Clan."
Susumu_Jaru = Personality(
    card_id=11607,
    title="Susumu Jaru",
    force=1,
    chi=1,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Tanjin enters play for 1 less Gold if your Allegiance is Progressive.<br>Invest :g2:: Give another player's target card a <b>Clout </b>token.<br><b>Home Interrupt, :bow::</b> Increase the strength of the action's Fear effects by the number of Clout tokens in play."
Susumu_Tanjin = Personality(
    card_id=11608,
    title="Susumu Tanjin",
    force=0,
    chi=2,
    personal_honor=1,
    gold_cost=2,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Battle:</b> Bow one or two of Yasi's target unbowed Weapons. Make a Ranged Attack equal to their total Force Modifiers."
Yasi = Personality(
    card_id=11609,
    title="Yasi",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Resilient, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
