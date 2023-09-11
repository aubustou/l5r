from __future__ import annotations

from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import (
    Air,
    BitterLies,
    Bloodspeaker,
    Commander,
    Courtier,
    Experienced,
    Kensai,
    LoveLetter,
    Loyal,
    Magistrate,
    Martyr,
    Musician,
    Paragon,
    Samurai,
    Shugenja,
    TheMaskedMonkey,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"This counts as two cards when destroyed during battle resolution.<br><b>Tireless Open:</b> If you have targeted Aggushi & Janqu with a Political action this turn, straighten them.<br><b>Battle, :bow::</b> Melee 3 Attack."
Bayushi_Aggushi_Bayushi_Janqu = Personality(
    card_id=11920,
    title="Bayushi Aggushi & Bayushi Janqu",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Irezu has +1C if another player is Lion Clan.<br><b>Battle:</b> Move home a target unit whose total Force is less than or equal to Irezu's Chi."
Bayushi_Irezu_Experienced = Personality(
    card_id=11921,
    title="Bayushi Irezu",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Commander, Experienced("1"), Martyr],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Iyashi has Courtier while you control The Sorrow.<br><b>Battle, :bow::</b> Melee 2 Attack, or Melee 4 Attack if you control The Sorrow or the target is Shadowlands."
Bayushi_Iyashi_Lady_Sorrow = Personality(
    card_id=11922,
    title="Bayushi Iyashi, Lady Sorrow",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Loyal, Magistrate, Musician, Paragon, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> After you Recruit Yamazaki, show a random card in another player's hand.<br><b>Political Open, :bow::</b> Rehonor and bow a target dishonorable Personality."
Shosuro_Yamazaki_the_Master_Courtier = Personality(
    card_id=11923,
    title="Shosuro Yamazaki, the Master Courtier",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, LoveLetter],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After a dishonorable Personality is destroyed, his controller loses 1 Honor.<br><b>:bow::</b> Produce Gold equal to Chijin's Chi which can only pay for a single Air or Maho Spell."
Yogo_Chijin = Personality(
    card_id=11924,
    title="Yogo Chijin",
    force=0,
    chi=4,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Bloodspeaker, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Courtesy: Gorobei has <b>Conqueror</b>. <i>(Courtesy traits do not take effect if you went first.)</i><br>Gorobei has +1F while in an army with a Crab Clan Personality."
Yogo_Gorobei = Personality(
    card_id=11925,
    title="Yogo Gorobei",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Magistrate, Samurai, TheMaskedMonkey, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
