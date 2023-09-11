from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Destined,
    Duelist,
    Expendable,
    Fire,
    Kensai,
    Magistrate,
    Monk,
    Samurai,
    Shadowlands,
    Shugenja,
    Smith,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Unstoppable Battle:</b> Fear 3, or Fear 4 if Takahide has won a duel this turn. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Daigotsu_Takahide = Personality(
    card_id=11926,
    title="Daigotsu Takahide",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Fire Open, :g3::</b> Create a +2F/+1C <b>One-Handed &#149; Sword &#149; Weapon</b> Item and attach it to your target Personality."
Gyushi_Kageto = Personality(
    card_id=11927,
    title="Gyushi Kageto",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Artisan, Fire, Shugenja, Smith],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card. Kensai may attach two Weapons, as long as neither is Two-Handed.)</i>"
Kokujin_Dairu_Student_of_the_Dark_Lotus = Personality(
    card_id=11928,
    title="Kokujin Dairu, Student of the Dark Lotus",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[Destined, Kensai, Monk, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Tireless Battle:</b> Bow your target unbowed Dragon Clan or Monk Personality to straighten Kuchika. You may destroy the target to give Kuchika +2F and permanently give her <b>Tattooed</b>."
Kokujin_Kuchika_Blood_of_the_Dark_Lotus = Personality(
    card_id=11929,
    title="Kokujin Kuchika, Blood of the Dark Lotus",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[Kensai, Monk, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Courtesy: You have a +5 Lobby Bonus. <i>(Courtesy traits do not take effect if you went first.)</i><br><b>Interrupt:</b> After you Recruit Issei, put a Political Battle Strategy from your discard pile into your hand."
Susumu_Issei = Personality(
    card_id=11930,
    title="Susumu Issei",
    force=0,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i> <br>Kengo has +1PH <i>(in and out of play)</i> if another player is Crab Clan."
Susumu_Kengo = Personality(
    card_id=11931,
    title="Susumu Kengo",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Expendable, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
